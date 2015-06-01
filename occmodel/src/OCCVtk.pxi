
def shapeToActor(Base occShape):

    cdef c_OCCBase *_occShape = <c_OCCBase *>occShape.thisptr

    return <object>c_shapeToActor(_occShape)