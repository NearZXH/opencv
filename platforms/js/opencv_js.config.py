# Classes and methods whitelist
core = {'': ['flip']}

imgproc = {'': ['cvtColor', 'getPerspectiveTransform', 'warpPerspective', 'resize']}

objdetect = {'': ['']}

video = {'': ['']}

dnn = {'dnn_Net': ['']}

features2d = {'Feature2D': ['']}

photo = {'': ['']}

aruco = {'': ['DetectorParameters', 'detectMarkers', 'drawDetectedMarkers'],
        'aruco_Dictionary': ['get'],
        }

calib3d = {'': ['']}

white_list = makeWhiteList([core, imgproc, objdetect, video, dnn, features2d, photo, aruco, calib3d])
