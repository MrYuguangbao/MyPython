class CourseList(object):
    def __init__(self, courseParentId,
                 courseChildId,
                 courseType,
                 coursePackId,
                 courseName,
                 courseDuration,
                 courseEnlist,
                 coursePrice,
                 createTime,
                 updateTime
                 ):
        self.courseParentId = courseParentId
        self.courseChildId = courseChildId
        self.courseType = courseType
        self.coursePackId = coursePackId
        self.courseName = courseName
        self.courseDuration = courseDuration
        self.courseEnlist = courseEnlist
        self.coursePrice = coursePrice
        self.createTime = createTime
        self.updateTime = updateTime


class CourseTeacherMapping(object):
    def __init__(self, coursePackId,
                 courseId,
                 className,
                 classDuration,
                 teacherName,
                 jobType,
                 remainNums,
                 classPrice,
                 createTime,
                 updateTime
                 ):
        self.coursePackId = coursePackId
        self.courseId = courseId
        self.className = className
        self.classDuration = classDuration
        self.teacherName = teacherName
        self.jobType = jobType
        self.remainNums = remainNums
        self.classPrice = classPrice
        self.createTime = createTime
        self.updateTime = updateTime


class GrabDashboard(object):
    def __init__(self,
                 courseId,
                 courseName,
                 courseTotal,
                 createTime,
                 updateTime):
        self.courseId = courseId
        self.courseName = courseName
        self.courseTotal = courseTotal
        self.createTime = createTime
        self.updateTime = updateTime


class CourseTeacherInfo(object):
    def __init__(self,
                 courseId,
                 teacherName,
                 rate,
                 note,
                 createTime,
                 updateTime):
        self.courseId = courseId
        self.teacherName = teacherName
        self.rate = rate
        self.note = note
        self.createTime = createTime
        self.updateTime = updateTime