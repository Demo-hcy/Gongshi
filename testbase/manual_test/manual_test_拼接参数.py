from library.common import *
from library.mqtt_lib.TSL_model.AIHub001_MODEL import AIHub001

ai = AIHub001('111')
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
ai1 = AIHub001('111')
ai1.services.addCamera.parameters.cameraInfoList.v = p.v
pprint(ai1.services.addCamera.parameters.cameraInfoList.v)