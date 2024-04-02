#! /usr/bin/python2
# coding: UTF-8

import os
import time
import sys
import json
import base64
import time
import httplib
import urlparse
import time
import urllib
import math
import traceback


def gethttptxt(url, data=None, header=None):
    """
    HTTP网络请求 方法

    :param url: 请求的url地址
    :param data: post参数，或者post数据
    :param header: 头信息，字典类型
    :returns: 请求返回结果
    :raises Exception: 请求异常
    """

    pas = urlparse.urlparse(url)
    host = pas.hostname
    port = pas.port if pas.port else (443 if pas.scheme == 'https' else 80)
    path = pas.path + (('?' + pas.query) if pas.query else '')
    body = data
    hconn = {}
    if pas.scheme == 'https':
        hconn = httplib.HTTPSConnection(host, port)
    else:
        hconn = httplib.HTTPConnection(host, port)

    hconn.connect()
    method = 'POST' if data else 'GET'
    if method == 'POST' and isinstance(body, dict):
        body = urllib.urlencode(body)

    headers = {
        'Accept-Charset': 'utf-8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'close',
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36' +
                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }

    if header:
        for key in header:
            headers[key] = header[key]

    hconn.request(method, path, body, headers)
    content = hconn.getresponse()
    if content.status != 200:
        raise Exception, 'Error: HTTP[%s]%s:\n%s\n' % (content.status, url, content.msg)
    strhtml = content.read()
    hconn.close()

    return strhtml

def gethttpjson(url, data=None, header=None):
    rs = gethttptxt(url, data, header)
    return json.loads(rs)

def download(url,outf,head='') :
    if os.path.isfile(outf) :
        toLog("File already download:" + outf)
        return
    cmd = "wget -T 30 -t 2 %s -qO '%s' '%s'" % (head,outf,url)
    toLog(cmd)
    os.system(cmd)
    pass

def download_hw(url,outf) :
    rs = gethttpjson(url)
    head = ''
    if rs and rs['dat'] and rs['dat']['url']  and rs['dat']['head']:
        url = rs['dat']['url']
        for k,v in rs['dat']['head'].items() :
            head += " --header='%s: %s' " % (k,v)
        download(url,outf,head)

def fit2csv(fname) :
    path = os.path.realpath(os.path.dirname(fname) + "/..")
    cmd = "java -jar '%s/src/FitCSVTool.jar' '%s' " % (path,fname)
    toLog(cmd)
    os.system(cmd)
    return fname.replace('.fit','.csv')


def csv2zip(fname) :
    dats = {}
    tname = fname.replace('.csv','.txt')
    zname = fname.replace('.csv','.zip')
    rtns  = False
    with open(fname) as f :
        for l in f :
            try :
                _d = formatData(l)
            except Exception as e:
                toLog('ERR:'+l)
                # sys.exit(0)
            if _d :
                for k,v in _d.items() :
                    if k not in dats :
                        dats[k] = []
                    dats[k].append(v)

    reclen = len(dats['record']) if 'record' in dats else 0
    if reclen > 100 :
        uid, tid = (fname.split('skid-')[1].split('_'))
        dats = processData(dats,uid,tid.split('.')[0])
        ms = data2json(dats['record'])
        p,f = tname.split('skid-',1)
        tname = p + f.replace('_', '') # 生成和前端相同的命名规则
        if len(ms) < 100 :
            toLog('txt strlen %d' % len(ms))
            return rtns
        try :
            f = open(tname,'w')
            f.write(ms)
        finally :
            f.close()
        cmd = "zip -qj '%s' '%s'" % (zname,tname)
        toLog(cmd)
        os.system(cmd)
        dats['session']['res_url'] = 'upload_goski/u/Fit2CSV/Data/skid-' + zname.split('skid-',1)[1]
        return  dats
    toLog('ERR: txt array size %d' % reclen)
    return rtns


def processData(dats,uid,tid):
    longitude = 0.0
    latitude  = 0.0
    avgangle  = []
    maxfall   = 0.0
    avgfall   = []
    skiCount  = len(dats['lap'])
    itemsnum  = len(dats['record']) - 1
    tms       = 0
    maxAltitude = 0
    for x in range(itemsnum) :
        cr = dats['record'][x]
        if x == 0 :
            cr['uid'] = uid
            cr['skiId'] = tid
        x+=1
        nx = dats['record'][x]
        nx['idx'] = x
        nx['uid'] = uid
        nx['skiId'] = tid
        nx['durationTime'] = nx['collectTime'] - cr['collectTime']
        nx['altitudeChange'] = nx['altitude'] - cr['altitude']
        nx['distance'] = round(nx['skiDistance'] - cr['skiDistance'],3)
        maxAltitude = max(maxAltitude,nx['altitude'])
        for y in range(skiCount):
            l = dats['lap'][y]
            l['uid'] = uid
            l['skiId'] = tid
            if cr['collectTime'] >= l['start_time'] and cr['collectTime'] <= l['end_time'] :
                cr['runCount'] = y+1
                cr['skiType'] = 1
                l['maxAltitude'] = max(l['maxAltitude'],cr['altitude'])
                if l['maxAltitude'] != tms  and 'device_info' not in dats:
                    tms = l['maxAltitude']
                    l['minAltitude'] = tms
                    for i in range(x-2,-1,-1):
                        if dats['record'][i]['runCount'] == cr['runCount']:
                            dats['record'][i]['runCount'] = 0
                            dats['record'][i]['skiType'] = 0
                        else :
                            break
                else :
                    l['minAltitude'] = min(l['minAltitude'] or cr['altitude'],cr['altitude'])
                    l['fall'] = l['maxAltitude'] - l['minAltitude']
                if not longitude :
                    longitude = nx['longitude']
                    latitude = nx['latitude']
                if not l['longitude'] or not l['latitude']:
                    l['longitude'] = nx['longitude']
                    l['latitude'] = nx['latitude']
                if nx['distance'] > 0 and nx['altitudeChange'] < 0 and abs(nx['altitudeChange']) < nx['distance']:
                    _lx = 1 * math.atan(abs(nx['altitudeChange']/nx['distance'])) * 180 / math.pi
                    nx['angle'] = 0
                    if _lx < 35.6 and _lx > 8 :
                        nx['angle'] = _lx
                        avgangle.append(nx['angle'])
                break
        cr['collectTime'] = strftime(int(cr['collectTime']))
        if x == itemsnum :
            nx['collectTime'] = strftime(int(nx['collectTime']))
    
    
    
    if skiCount > 0 :
        for v in dats['lap'] :
            maxfall = max(maxfall,v['fall'])
            avgfall.append(v['fall'])
    dats['session'] = dats['session'][0]
    # dats = dats['record']
    avgangle.sort(reverse = True)
    dats['session']['skiId'] = "%s%s" % (str(uid),str(tid))
    dats['session']['uid'] = uid
    dats['session']['skiCount'] = max(dats['session']['skiCount'],skiCount)
    dats['session']['maxAngle'] = sum(avgangle[3:20]) / (len(avgangle[3:20]) or 1)
    dats['session']['avgAngle'] = sum(avgangle) / len(avgangle)
    dats['session']['longitude'] = longitude
    dats['session']['latitude'] = latitude
    dats['session']['totalFall'] =  sum(avgfall)
    dats['session']['maxFall'] = maxfall
    dats['session']['avgFall'] = dats['session']['totalFall'] / (len(avgfall) or 1)
    dats['session']['maxAltitude'] = maxAltitude
    return dats


def data2json(dats) :
    ms = json.dumps(dats)
    return ms


def formatData(dat) :
    dat = dat.strip().replace('"','').split(',')
    sdat = {}
    if 'Data' != dat[0] or dat[2] not in ['device_info','record','lap','session']:
        return {}
    deftype = dat[2]
    for i in range(0,len(dat),3):
        k = dat[i]
        if k :
            sdat[k] = dat[i+1:i+3]
        else :
            break
    fdat = {
        'device_info' : {
            'product_name' : ['!product_name','str','']
        },
        'record' : {
            "acceleration": ['','',0.0],  # 加速度
            "altitude":     ['!enhanced_altitude,altitude','float',0.0],  # 海拔
            "altitudeChange": ['','',0.0],     # 海拔差
            "angle": ['','',0.0],              # 坡角
            "appVersion": ['','',"COROS,(515)"],
            "collectTime": ['timestamp','time',0.0],
            "distance":['','float',0.0],           # 距离
            "durationTime":['','',0],       # 持续时间
            "horizontalAccuracy":['','',0],
            "idx":['','',0],
            "latitude":['!position_lat','semicircles',0],
            "longitude":['!position_long','semicircles',0],
            "maxAltitude":['','',0],        # 最高海拔
            "ranchId":['','',0],
            "runCount":['','',0],
            "skiDistance":['distance','float',0.0],        # 累计滑行距离
            "skiFall":['','',0],
            "skiId":['','',0],
            "skiTotalTime":['','',0],       # 滑行总时间
            "skiType":['','',0],
            "speed":['enhanced_speed,speed','m/s',0.0],              # 速度
            "sportsType":['','',0],
            "sumTotalDistance":['','',0.0], # 总距离
            "uid":['','',0],
            "heartRate" : ['heart_rate','int',0],
            "verticalAccuracy":['','',0.0]
        },
        'lap' : {
            'skiId' : ['','',0],
            'start_time':['start_time','time',0],
            'end_time' :['timestamp','time',0],
            'distance':['total_descent','float',0.0],
            'skiCount' :['','',0],
            'uid'     : ['','',0],
            'ranchId' : ['','',0],
            'longitude' : ['start_position_long','semicircles',0],
            'latitude' : ['start_position_lat','semicircles',0],
            'fall' : ['','',0],
            'maxAltitude' : ['','',0],
            'minAltitude' : ['','',0],
            'maxAngle' : ['','float',0.0],
            'maxSpeed' : ['enhanced_max_speed,max_speed','m/s',0],
            'avgSpeed' : ['enhanced_avg_speed,avg_speed','m/s',0],
            'maxHeartRate' : ['max_heart_rate','int',0],
            'avgHeartRate' : ['avg_heart_rate','int',0],
            'calorie' : ['total_calories,','',0],
        },
        'session' : {
            'skiId':['','',0],
            'uid':['','',0],
            'distance':['total_distance','float',0.0],
            'maxSpeed':['max_speed,enhanced_max_speed','m/s',0.0],
            'avgSpeed':['avg_speed,enhanced_avg_speed','m/s',0.0],
            'maxAngle':['','float',0.0],
            'avgAngle':['','float',0.0],
            'maxFall':['','float',0.0],
            'avgFall':['','float',0.0],
            'totalFall':['','float',0.0],
            'skiCount':['num_laps','',0],
            'totalTime':['total_elapsed_time','float',0],
            'effectiveTime':['total_timer_time','float',0],
            'maxAltitude':['','float',0.0],
            'longitude':['','float',0.0],
            'latitude':['','float',0.0],
            'locationName':['','',''],
            'sportsType':['','',1],
            'skiDate':['start_time','time',''],
            'ranchId':['','',1],
            'ranchIds':['','',''],
            'appVersion':['','',''],
            'skiTraceType':['','',0],
            'res_url':['','',''],
        }
    }
    dat = fdat[deftype].copy()
    for (k,v) in dat.items() :
        sk = v[0]
        if(sk) :
            _is = sk[0] == "!"
            if _is :
                sk = sk[1:]
            sk = sk.split(',')
            _sk = ''
            for _k in sk :
                if _k in sdat :
                    _sk = _k
                    break
            if _sk:
                _v = sdat[_sk][0]
                if v[1] == 'int' :
                    v[2] = int(_v)
                elif v[1] == 'float' :
                    v[2] = float(_v)
                elif v[1] == 'm/s' :
                    v[2] = round(float(_v) * 3.6,2)
                elif v[1] == 'time' :
                    v[2] = 631065600 + int(_v)
                elif v[1] == 'semicircles' :
                    v[2] = 180.0 / (1<<31) * int(_v)
                elif v[1] == 'str' :
                    v[2] = _v
            elif _is :
                return {}
        dat[k] = v[2]
    return {deftype : dat}

def getRanch(lat,lng):
    url = "http://ap.goski.cn/go?a=2008&op=ranch&lat=%s&lng=%s" % (str(lat),str(lng))
    rs = gethttptxt(url)
    toLog(url)
    rs = json.loads(rs)
    if rs and rs['st'] == 1:
        return rs['dat']
    return {}

def strftime(tm):
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(tm))

def toLog(msg) :   
    """ 输出日志函数 """ 
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " -- [" + '{}'.format(msg) + "]")
    pass

def hwJson2zip(jsonfile) :
    
    pass


def insert_dat(dats,l) :
    if dats and len(dats['lap']) > 0:
        # print(dats['session'])
        for k in dats['session']:
            dats['session'][k] = str(dats['session'][k])
        # 开始查询围栏数据
        rs = getRanch(dats['session']['latitude'],dats['session']['longitude'])
        if 'id' in rs:
            dats['session']['ranchId'] = rs['id'] 
            dats['session']['ranchIds'] = []
            dats['session']['locationName'] = rs['sr_name']
        for x in dats['lap']:
            rs = getRanch(x['latitude'],x['longitude'])
            if 'id' not in rs:
                continue
            x['ranchId'] = rs['id'] or dats['session']['ranchId']
            if x['ranchId'] not in dats['session']['ranchIds'] :
                dats['session']['ranchIds'].append(x['ranchId'])
        dats['session']['ranchIds'] = str(','.join(dats['session']['ranchIds']))
        sql = "UPDATE coros_task SET zipUrl = '%s' WHERE id = '%s'; " % (dats['session']['res_url'] if dats else 'no data', l['id'])
        sql = base64.b64encode(sql.encode('utf-8'))
        sql = gethttptxt("http://ap.goski.cn/go.php?a=2008&op=sql&db=", sql)
        if dats != False and len(str(dats['session']['res_url'])) > 10 :
            # 处理lap数据
            sql = []
            cols = ""
            for x in dats['lap']:
                x['start_time'] = strftime(int(x['start_time']))
                x['end_time'] = strftime(int(x['end_time']))
                cols = ','.join(x.keys())
                val  = "','".join([str(v) for v in x.values()])
                sql.append("('%s')" % val)
            if sql and cols :
                sql = "insert into usr_speed_lap ("+cols+") values "+ ",".join(sql)
                toLog(sql)
                sql = base64.b64encode(sql.encode('utf-8'))
                sql = gethttptxt("http://ap.goski.cn/go.php?a=2008&op=sql&db=", sql)
            
            # 处理session数据
            val = dats['session']
            val['skiDate'] = strftime(int(val['skiDate']))
            val['appVersion'] = l['deviceName']
            cols = ','.join(val.keys())
            val  = "','".join( [x.encode('utf-8','strict') for x in val.values()])
            sql = "insert into usr_speed (%s) values ('%s')" % (cols,val)
            toLog(sql)
            sql = base64.b64encode(sql)
            sql = gethttptxt("http://ap.goski.cn/go.php?a=2008&op=sql&db=", sql)

def main() :
    """ 主函数开始执行 """
    toLog('Start')
    pathStr = os.path.dirname(__file__)
    pathStr = os.path.realpath(pathStr)

    dats = {}
    startTime = strftime(time.time()-86400 * 10 )
    sql = "SELECT * FROM coros_task WHERE createTime > '%s' and deviceName='HUAWEI' and zipUrl is null LIMIT 50" % (startTime)
    # sql = "SELECT * FROM coros_task WHERE createTime > '%s' and zipUrl is null LIMIT 50" % (startTime)
    
    # 测试代码
    # sql = "SELECT * FROM coros_task WHERE id=237280158"
    
    sql   = base64.b64encode(sql.encode('utf-8'))
    sql   = gethttptxt("http://ap.goski.cn/go.php?a=2008&op=sql&db=", sql)
    datg  = json.loads(sql)
    if datg['dat'] and len(datg['dat']) > 0 :
        for l in datg['dat'] :
            times = time.mktime(time.strptime(l['startTime'],'%Y-%m-%d %H:%M:%S'))
            try :
                if l['deviceName'] in ['HUAWEI'] :
                    outf = '%s/Data/%s.json' % (pathStr,l['id'])
                    download_hw(l['fitUrl'],outf)
                    dats = hwJson2zip(outf)
                    continue
                    # insert_dat(dats,l)
                else :
                    skid = 'skid-%s_%d' % (l['uid'], times)
                    outf = '%s/Data/%s.fit' % (pathStr,skid)
                    download(l['fitUrl'],outf)
                    outcf = fit2csv(outf) # 生产csv
                    dats = csv2zip(outcf) # 处理数据，生产zip文件
                    insert_dat(dats,l)
            except Exception as e:
                traceback.print_exc()
                continue
    else :
        toLog('no data')
    toLog('Finished')


def lock(lck) :
    """ 判读是否已经有进程在执行 """
    toLog("LCK:" + str(lck))
    _fn = os.path.realpath(__file__)
    _fn = os.path.dirname(_fn) + "/." + os.path.basename(_fn)
    _fn += ".lock"
    if not lck :
        if os.path.isfile(_fn) :
            os.unlink(_fn)
        return
    if os.path.isfile(_fn) :
        toLog("Task is running! Exit now")
        sys.exit(0)
    with open(_fn,'w') as _fh :
        _fh.write(str(os.getpid()))


if __name__ == '__main__':
    try:
        lock(True)
        # _rtime = time.perf_counter()
        main()
    except Exception as e:
        traceback.print_exc()
    finally :
        lock(False)
        # print("Script Finished, Use Time:",time.perf_counter()-_rtime)
        pass


