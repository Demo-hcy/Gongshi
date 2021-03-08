from library.common import *
from library.mqtt_lib.TSL_model.S9_7G_AI_MODEL import S9_QG_AI

ai = S9_QG_AI('111')
p = ai.services.addCamera.parameters.cameraInfoList

A = type(p.columnComplex[0])
a = A()
a.cameraId.v = 'xxx'
a.cameraUrl.v = 'sss'
a.pushRtsp.v = 'dddd'

l = []
l.append(a)
p.columnComplex = l

pprint({p.id: p.v})
ai1 = S9_QG_AI('111')
ai1.services.addCamera.parameters.cameraInfoList.v = p.v
pprint(ai1.services.addCamera.parameters.cameraInfoList.v)