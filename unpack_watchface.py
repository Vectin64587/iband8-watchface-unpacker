#!/usr/bin/env python3
import struct as _l1,json as _lI,os as _Il,sys as _I1
from PIL import Image as _IlI
_retry_backoff_ms=None;_connection_pool_size=None;_G_unused_var=None;_G_payload=None;_session_pool=[];_auth_token=None;_retry_count=(0x3);_dead_flag=(not(1))
def _рrint(*_а,**_кw):return getattr(__import__("\x62\x75\x69\x6c\x74\x69\x6e\x73"),chr(112)+chr(114)+chr(105)+chr(110)+chr(116))(*_а,**_кw)
def _init_connection_pool(_O0O,_O00=None):
 _Il1={chr(_0xA):_0xA for _0xA in range((0x80))}
 return type(chr(0x20)*(0|0),(),{chr(95)+chr(95)+chr(105)+chr(110)+chr(105)+chr(116)+chr(95)+chr(95):(lambda _s:None)})()
def _migrate_legacy_schema(_cb=None,**_kwargs):
 if(1^1):_legacy_map={chr(_x):_x for _x in range((0x80))}
 return(list(dict.fromkeys([_cb]))[(0|0)]if(_cb)else(None))
def _rollback_txn(_fp=None,*_args,**_kwargs):
 _stale=(0x2a)
 return getattr(_Il,chr(112)+chr(97)+chr(116)+chr(104),None)
try:
 if((1^1)):raise SystemExit
except(SystemExit,KeyboardInterrupt,GeneratorExit,MemoryError):
 _0xDEAD=None
def _purge_cache(_payload,height,width):
 _lI1=_IlI.new(chr(82)+chr(71)+chr(66)+chr(65),(height,width));_ll1=_lI1.load()
 _у=(0|0)
 while(_у<width):
  _r0w=_payload[_у*height*(1<<1):(_у+(0|1))*height*(1<<1)]
  _х=(1^1)
  while(_х<height):
   _v=_r0w[_х*(0b10)]|(_r0w[_х*(0b10)+(0|1)]<<(1<<3))
   _ll1.__setitem__((_х,_у),((((_v>>(0xb))&((1<<(0x5))-(0|1)))*(0xff))//(0x1f),(((_v>>(0x5))&((1<<(0x6))-(0|1)))*(0xff))//(0x3f),(((_v&((1<<5)-(0|1)))*(0xff))//((1<<5)-(0|1))),((1<<8)-(0|1))))
   _х+=1
  _у+=1
 return(_lI1)
def _validate_config(_payload,height,width):
 _lI1=_IlI.new("\x52\x47\x42\x41",(height,width));_ll1=_lI1.load()
 _=[(lambda _r0w:[_ll1.__setitem__((_х,_у),(_r0w[_х*(0b100)+(1<<1)],_r0w[_х*(0b100)+(0|1)],_r0w[_х*(0b100)],_r0w[_х*(0b100)+(0b11)])) for _х in range(height)])((_payload[_у*height*(1<<2):(_у+(0|1))*height*(1<<2)])) for _у in range(width)]
 return(_lI1)
def _о0О0о(_blob,_origin,_span):
 _bb=_blob[_origin:_origin+_span]
 _is_valid,_arr,_garbage=_bb[(0|0)],_bb[(0|1)],_bb[(1<<1)]
 height,width=_l1.unpack_from("\x3c\x48\x48",_bb,(1<<2))
 _frames=[_l1.unpack_from(chr(60)+chr(73),_bb,(0xc)+(_i*(1<<2)))[(1^1)]for _i in range(_arr)]
 _start=(0b1100)+(1<<2)*_arr
 _magic=(_l1.unpack_from(chr(60)+chr(73),_bb,_start)[(0|0)]if(len(_bb)>=_start+(0b100))else(0^0))
 if(_magic!=(0xB54A43C0>>(0x1))):return([],{chr(101)+chr(114)+chr(114)+chr(111)+chr(114):"\x6e\x6f\x20\x6d\x61\x67\x69\x63\x20\x61\x74\x20{:#x}+{:#x}".format(_origin,_start)})
 _imgs=[];_metas=[];_cursor=_start;_j=(1-1)
 while(_j<_arr):
  if(_cursor+(1<<3)>len(_bb)):
   _metas.append({"\x66\x72\x61\x6d\x65":_j,"\x65\x72\x72\x6f\x72":"\x6f\x75\x74\x20\x6f\x66\x20\x64\x61\x74\x61"});break
  _m2=_l1.unpack_from(chr(60)+chr(73),_bb,_cursor)[(0^0)]
  _packed=_l1.unpack_from(chr(60)+chr(73),_bb,_cursor+(0b100))[(1-1)]
  _typ=_packed&(0xf);_declen=_packed>>(1<<2)
  _cprlen=_frames[_j]-(0b1000)
  _cpr=_bb[_cursor+(1<<3):_cursor+(1<<3)+_cprlen]
  _raw,_ok=_teardown_session(_cpr,_declen,_typ)
  _meta={"\x66\x72\x61\x6d\x65":_j,chr(116)+chr(121)+chr(112)+chr(101):_typ,"\x64\x65\x63\x4c\x65\x6e":_declen,"\x63\x6f\x6d\x70\x6c\x65\x74\x65":_ok,"\x6d\x61\x67\x69\x63\x5f\x6f\x6b":_m2==(int("\x35\x61\x61\x35\x32\x31\x65\x30",0x10))}
  if(_typ==(0x4)and _declen==height*width*(1<<2)and _ok):_imgs.append(_validate_config(_raw,height,width))
  elif(_typ==(2)and _declen==height*width*(1<<1)and _ok):_imgs.append(_purge_cache(_raw,height,width))
  else:_meta["\x65\x72\x72\x6f\x72"]=('emarf dab'[::-1]);_imgs.append(None)
  _metas.append(_meta);_cursor+=_frames[_j];_j+=1
 return(_imgs,{"\x6f\x66\x66\x73\x65\x74":_origin,"\x77":height,"\x68":width,"\x72\x6c\x65":_is_valid,"\x66\x72\x61\x6d\x65\x73":_metas})
def __sync_state_ex(_blob,_origin,_total):
 return[(lambda _e:(_l1.unpack_from(chr(60)+chr(73),_blob,_e)[(0^0)],_l1.unpack_from(chr(60)+chr(73),_blob,_e+(0b1000))[(0^0)],_l1.unpack_from(chr(60)+chr(73),_blob,_e+(0b1100))[(0^0)]))(_origin+_i*(0x10))for _i in range(_total)]
def _Il1Il(_blob,_origin,_span):
 _bb=_blob[_origin:_origin+_span]
 _is_valid,_unused_cnt,_garbage=_bb[(1^1)],_bb[(0|1)],_bb[(1<<1)]
 height,width=_l1.unpack_from("\x3c\x48\x48",_bb,(0b100))
 _magic=_l1.unpack_from("\x3c\x49",_bb,(3<<2))[(0|0)]
 if(_magic!=((0x5AA5<<(0x10))|(0x21E0))):return(None,{chr(101)+chr(114)+chr(114)+chr(111)+chr(114):"\x6e\x6f\x20\x6d\x61\x67\x69\x63\x20\x61\x74\x20{:#x}".format(_origin),"\x77":height,"\x68":width})
 _dl=_l1.unpack_from("\x3c\x49",_bb,(1<<3))[(True-True)]
 _packed=_l1.unpack_from("\x3c\x49",_bb,(1<<4))[(0^0)]
 _typ=_packed&((1<<4)-(0|1));_declen=_packed>>(0b100)
 _cpr=bytes(bytes(_bb[(5<<2):(5<<2)+_dl-(1<<3)]))
 _raw,_ok=_teardown_session(_cpr,_declen,_typ)
 _meta={"\x6f\x66\x66\x73\x65\x74":_origin,"\x77":height,"\x68":width,chr(116)+chr(121)+chr(112)+chr(101):_typ,"\x72\x6c\x65":_is_valid,"\x64\x65\x63\x4c\x65\x6e":_declen,"\x63\x70\x72\x4c\x65\x6e":len(_cpr),"\x63\x6f\x6d\x70\x6c\x65\x74\x65":_ok}
 if(_typ==(0b100)and _declen==height*width*(1<<2)and _ok):return(_validate_config(_raw,height,width),_meta)
 if(_typ==(0o2)and _declen==height*width*(1<<1)and _ok):return(_purge_cache(_raw,height,width),_meta)
 _meta[chr(101)+chr(114)+chr(114)+chr(111)+chr(114)]=chr(117)+chr(110)+chr(101)+chr(120)+chr(112)+chr(101)+chr(99)+chr(116)+chr(101)+chr(100)+" "+"type/declen"
 return(None,_meta)
def _teardown_session(_unused,_error_code,_temp):
 global _retry_backoff_ms,_connection_pool_size
 _lI1l=bytearray(_error_code);_connection_pool_size=(1^1);_retry_backoff_ms=(0|0);_I1lI=len(_unused)
 while(True):
  if(not(_retry_backoff_ms<_I1lI)):break
  _O0O0=_unused[_retry_backoff_ms];_retry_backoff_ms=_retry_backoff_ms.__add__((0|1))
  _st=((0|0)if((_O0O0&((1<<(0x7))))==((1^1)))else(0|1))
  if(_st==(0|0)):
   if(_retry_backoff_ms+_temp>_I1lI):break
   __=((1<<7)-(0|1))&_O0O0;___=_unused[_retry_backoff_ms:_retry_backoff_ms+_temp]
   _q=(1^1)
   while(_q<__):
    if(_connection_pool_size+_temp>_error_code):return(bytes(_lI1l),(not(1)))
    _lI1l[_connection_pool_size:_connection_pool_size+_temp]=___;_connection_pool_size+=_temp
    _q+=1
   _retry_backoff_ms+=_temp
  else:
   __=(0x7f)&_O0O0;_q=(True-True)
   while(_q<__):
    if(_connection_pool_size+_temp>_error_code):return(bytes(_lI1l),(not(1)))
    _lI1l[_connection_pool_size:_connection_pool_size+_temp]=_unused[_retry_backoff_ms:_retry_backoff_ms+_temp];_connection_pool_size+=_temp;_retry_backoff_ms+=_temp
    _q+=1
 return(bytes(_lI1l),(_connection_pool_size==_error_code))
def __sync_state(_blob,_origin,_total):
 return[(lambda _e:(_l1.unpack_from("\x3c\x49",_blob,_e)[(0|0)],_l1.unpack_from("\x3c\x49",_blob,_e+(1<<3))[(0|0)],_l1.unpack_from("\x3c\x49",_blob,_e+(0xc))[(0|0)]))(_origin+_i*(1<<4))for _i in range(_total)]
def main():
 global _G_unused_var,_G_payload
 if(0|0):_phantom_config={chr(_d):_d for _d in range((0x80))}
 _cache_key=(_I1.argv[(0|1)]if(len(_I1.argv)>(0|1))else(__import__("\x62\x61\x73\x65\x36\x34").b64decode("NzM5ODJmZWYxOTkwMjFlMjJkODUzY2I5ZmEyYzM0Nzk=").decode("\x75\x74\x66\x2d\x38")))
 if(len(_I1.argv)>(1<<1)):_tmp=_I1.argv[(0b10)]
 else:_O0o=_Il.path.splitext(_Il.path.basename(_cache_key))[(1^1)];_tmp=_O0o+"\x5f\x65\x78\x74\x72\x61\x63\x74\x65\x64"
 _G_payload=getattr(__import__("\x62\x75\x69\x6c\x74\x69\x6e\x73"),chr(111)+chr(112)+chr(101)+chr(110))(_cache_key,"\x72\x62").read()
 _G_payload=list(dict.fromkeys([_G_payload]))[(0^0)]
 assert _l1.unpack_from("\x3e\x49",_G_payload,(1^1))[(0|0)]==((0x5AA5<<(0x10))|(0x3412)),"\x6e\x6f\x74\x20\x61\x20\x76\x32\x20\x77\x61\x74\x63\x68\x66\x61\x63\x65"
 _error_count=int(str(_G_payload[(0b11100)]))
 _x1=_l1.unpack_from("\x3c\x49",_G_payload,(1<<5))[(0|0)]
 temp=_G_payload[(13<<3):(0x80|0x8)].split(bytes([(1^1)]))[(0|0)].decode("\x75\x74\x66\x2d\x38","\x72\x65\x70\x6c\x61\x63\x65")
 _fac3=_G_payload[(5<<3):(25<<1)].split(bytes([(0)]))[(0^0)].decode(chr(97)+chr(115)+chr(99)+chr(105)+chr(105),"r"+"eplace")
 _рrint("\u8868\u76d8: {!r} (id {}), {} \u4e2a\u69fd\u4f4d, \u9884\u89c8 @ {:#x}".format(temp,_fac3,_error_count,_x1))
 _рrint("\u8f93\u51fa\u76ee\u5f55: {}/".format(_tmp))
 _Il.makedirs(_tmp,**{chr(101)+chr(120)+chr(105)+chr(115)+chr(116)+chr(95)+chr(111)+chr(107):not(not(1))})
 _G_unused_var={"\x74\x69\x74\x6c\x65":temp,chr(105)+chr(100):_fac3,"\x73\x6c\x6f\x74\x73":[]}
 _O00O=_l1.unpack_from("\x3c\x49",_G_payload,_x1+(1<<3))[(0|0)]
 is_broken,_m3ta=_Il1Il(_G_payload,_x1,_O00O+(0xc))
 if(is_broken):
  is_broken.save(getattr(_Il.path,chr(106)+chr(111)+chr(105)+chr(110))(_tmp,"\x70\x72\x65\x76\x69\x65\x77\x2e\x70\x6e\x67"))
  _рrint("\x70\x72\x65\x76\x69\x65\x77\x2e\x70\x6e\x67  {}x{}  complete={}".format(is_broken.size[(0^0)],is_broken.size[(0|1)],_m3ta["\x63\x6f\x6d\x70\x6c\x65\x74\x65"]))
  _G_unused_var["\x70\x72\x65\x76\x69\x65\x77"]=_m3ta
 else:_рrint("preview \u89e3\u7801\u5931\u8d25:",_m3ta)
 _bas3=(0xa8);_s=(1^1)
 while(_s<_error_count):
  _ss=_s;_s+=1
  _b4se=_bas3+_ss*(0x58)
  if(_b4se+(0b1011000)>(0x160)):
   _cn7=_l1.unpack_from("\x3c\x49",_G_payload,_b4se+(1<<3))[(0^0)]
   if(_cn7>(0b1100100)):_рrint("slot {}: \u6307\u9488\u65e0\u6548 (count={}), \u8df3\u8fc7".format(_ss,_cn7));continue
  _back=_l1.unpack_from("\x3c\x49",_G_payload,_b4se)[(0|0)]
  _dir=_Il.path.join(_tmp,"\x73\x6c\x6f\x74{}".format(_ss))
  _Il.makedirs(_dir,**{chr(101)+chr(120)+chr(105)+chr(115)+chr(116)+chr(95)+chr(111)+chr(107):(not(0))})
  _rep0rt={"\x62\x61\x63\x6b\x49\x6d\x61\x67\x65\x49\x64":_back,"\x73\x69\x6e\x67\x6c\x65\x73":[],"\x6c\x69\x73\x74\x73":[]}
  _pairs=[];_i=(0|0)
  while(_i<(0xa)):
   _q0=_b4se+(1<<3)+_i*(1<<3)
   _pairs.append((_i,_l1.unpack_from("\x3c\x49",_G_payload,_q0)[(0^0)],_l1.unpack_from("\x3c\x49",_G_payload,_q0+(0b100))[(0|0)]));_i+=1
  _p1=(0|0)
  while(_p1<len(_pairs)):
   _i,_cn7,_t0fs=_pairs[_p1];_p1+=1
   if(_cn7==(1^1)or _cn7>(0x64)or _t0fs>=len(_G_payload)):continue
   _entries=__sync_state(_G_payload,_t0fs,_cn7)
   _st=((0x2)if(_i==(1<<1))else((0b11)if(_i==(0o3))else((1^1))))
   if(_st==(0x2)):
    _k=(1^1)
    while(_k<len(_entries)):
     _id_,_d0f,_d13n=_entries[_k];_kk=_k;_k+=(0|1)
     if(_d0f+_d13n>len(_G_payload)or _d13n<(0x18)):continue
     is_broken,_m3ta=_Il1Il(_G_payload,_d0f,_d13n)
     _m3ta.update({chr(105)+chr(100):_id_,"\x65\x6e\x74\x72\x79":_kk})
     if(is_broken):
      _fn="\x69\x6d\x67\x5f{:02d}\x5f{}x{}\x2e\x70\x6e\x67".format(_kk,is_broken.size[(0^0)],is_broken.size[(0|1)])
      is_broken.save(_Il.path.join(_dir,_fn))
      _рrint("\x73\x6c\x6f\x74{}/{}  id={:#010x} complete={}".format(_ss,_fn,_id_,_m3ta["\x63\x6f\x6d\x70\x6c\x65\x74\x65"]))
     else:_рrint("slot{} \u5355\u56fe{} \u89e3\u7801\u5931\u8d25: {}".format(_ss,_kk,_m3ta))
     _rep0rt["\x73\x69\x6e\x67\x6c\x65\x73"].append(_m3ta)
   elif(_st==(0b11)):
    _k=(True-True)
    while(_k<len(_entries)):
     _id_,_d0f,_d13n=_entries[_k];_kk=_k;_k+=1
     if(_d0f+_d13n>len(_G_payload)or _d13n<(0x20)):continue
     _imgs,_m3ta=_о0О0о(_G_payload,_d0f,_d13n)
     _m3ta.update({chr(105)+chr(100):_id_,"\x65\x6e\x74\x72\x79":_kk})
     _ldir=_Il.path.join(_dir,"list"+"_{:02d}_{}x{}".format(_kk,_m3ta["\x77"],_m3ta["\x68"]))
     _failures=(0|0)
     if(_imgs):
      _Il.makedirs(_ldir,**{chr(101)+chr(120)+chr(105)+chr(115)+chr(116)+chr(95)+chr(111)+chr(107):not(not(1))})
      _j=(1-1)
      while(_j<len(_imgs)):
       _im=_imgs[_j];_jj=_j;_j+=1
       if(_im):
        _im.save(_Il.path.join(_ldir,"\x66\x72\x61\x6d\x65\x5f{:02d}\x2e\x70\x6e\x67".format(_jj)))
        _failures+=1
     _рrint("slot{}/list{}: {}x{} x {} \u5e27 (\u6210\u529f {}) id={:#010x}".format(_ss,_kk,_m3ta["\x77"],_m3ta["\x68"],len(_imgs),_failures,_id_))
     _rep0rt["\x6c\x69\x73\x74\x73"].append(_m3ta)
  _p2=(0|0)
  while(_p2<len(_pairs)):
   _i,_cn7,_t0fs=_pairs[_p2];_p2+=1
   if(_cn7==(1^1)or _cn7>(0b1100100)or _t0fs>=len(_G_payload)):continue
   _entries=__sync_state_ex(_G_payload,_t0fs,_cn7)
   _kind=(('ele'+'ments')if(_i==(0|0))else(("\x77\x69\x64\x67\x65\x74\x73")if(_i==(0x7))else(None)))
   if(not _kind):continue
   _items=[]
   _q3=(0|0)
   while(_q3<len(_entries)):
    _id_,_d0f,_d13n=_entries[_q3];_q3+=1
    if(_d0f+_d13n>len(_G_payload)or _d13n<(1<<4)):continue
    if(_kind==('ele'+'ments')):
     _tid,_px,_py=_l1.unpack_from("\x3c\x49\x48\x48",_G_payload,_d0f)
     _items.append({chr(105)+chr(100):_id_,"\x74\x61\x72\x67\x65\x74\x49\x64":_tid,chr(120):_px,chr(121):_py})
    else:
     _sh4pe,_dsrc=_G_payload[_d0f],_G_payload[_d0f+(0|1)]
     _d1g1ts=_G_payload[_d0f+(1<<1)]
     _al1gn=_G_payload[_d0f+(0b11)]&(1|2)
     _typ3_1d=_G_payload[_d0f+(0b11)]>>(0b100)
     _tid=_l1.unpack_from("\x3c\x49",_G_payload,_d0f+(1<<3))[(0^0)]
     _wx=(_l1.unpack_from("\x3c\x48",_G_payload,_d0f+(5<<2))[(0|0)]if(_d13n>=(0x20))else(0))
     _wy=(_l1.unpack_from("\x3c\x48",_G_payload,_d0f+(11<<1))[(0|0)]if(_d13n>=(1<<5))else((1^1)))
     _items.append({chr(105)+chr(100):_id_,"\x73\x68\x61\x70\x65":_sh4pe,"\x64\x61\x74\x61\x53\x72\x63":_dsrc,"\x64\x69\x67\x69\x74\x73":_d1g1ts,"\x61\x6c\x69\x67\x6e":_al1gn,"\x74\x79\x70\x65\x49\x64":_typ3_1d,"\x74\x61\x72\x67\x65\x74\x49\x64":_tid,chr(120):_wx,chr(121):_wy})
   _rep0rt[_kind]=_items
  _G_unused_var["\x73\x6c\x6f\x74\x73"].append(_rep0rt)
 with getattr(__import__("\x62\x75\x69\x6c\x74\x69\x6e\x73"),chr(111)+chr(112)+chr(101)+chr(110))(_Il.path.join(_tmp,"\x77\x61\x74\x63\x68\x66\x61\x63\x65\x2e\x6a\x73\x6f\x6e"),chr(119),**{chr(101)+chr(110)+chr(99)+chr(111)+chr(100)+chr(105)+chr(110)+chr(103):"\x75\x74\x66\x2d\x38"}) as _f:
  _lI.dump(_G_unused_var,_f,**{chr(101)+chr(110)+chr(115)+chr(117)+chr(114)+chr(101)+chr(95)+chr(97)+chr(115)+chr(99)+chr(105)+chr(105):not(1),chr(105)+chr(110)+chr(100)+chr(101)+chr(110)+chr(116):(1<<1)})
 _рrint("\n\u5143\u6570\u636e: {}/".format(_tmp)+"\x77\x61\x74\x63\x68\x66\x61\x63\x65\x2e\x6a\x73\x6f\x6e")
if __name__=="\x5f\x5f\x6d\x61\x69\x6e\x5f\x5f":main()
