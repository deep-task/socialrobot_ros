[ control info ]
control_cycle = 10   # milliseconds

[ port info ]
# PORT NAME  | BAUDRATE | DEFAULT JOINT
/dev/ttyUSB_kist | 1000000  | LShoulder_Pitch
#/dev/ttyUSB0 | 1000000  | RShoulder_Pitch

[ device info ]
# TYPE    | PORT NAME    | ID   | MODEL         | PROTOCOL | DEV NAME        | BULK READ ITEMS
dynamixel | /dev/ttyUSB_kist | 1    | XM540-W270    | 2.0      | LShoulder_Pitch | present_position
dynamixel | /dev/ttyUSB_kist | 2    | XM540-W270    | 2.0      | LShoulder_Roll  | present_position
dynamixel | /dev/ttyUSB_kist | 3    | XM-430-W350   | 2.0      | LElbow_Pitch    | present_position
dynamixel | /dev/ttyUSB_kist | 4    | XM540-W270    | 2.0      | LElbow_Yaw      | present_position
dynamixel | /dev/ttyUSB_kist | 5    | XM-430-W350   | 2.0      | LWrist_Pitch    | present_position
dynamixel | /dev/ttyUSB_kist | 6    | XM-430-W350   | 2.0      | LFinger         | present_position
dynamixel | /dev/ttyUSB_kist | 7    | XM540-W270    | 2.0      | RShoulder_Pitch | present_position
dynamixel | /dev/ttyUSB_kist | 8    | XM540-W270    | 2.0      | RShoulder_Roll  | present_position
dynamixel | /dev/ttyUSB_kist | 9    | XM-430-W350   | 2.0      | RElbow_Pitch    | present_position
dynamixel | /dev/ttyUSB_kist | 10   | XM540-W270    | 2.0      | RElbow_Yaw      | present_position
dynamixel | /dev/ttyUSB_kist | 11   | XM-430-W350   | 2.0      | RWrist_Pitch    | present_position
dynamixel | /dev/ttyUSB_kist | 12   | XM-430-W350   | 2.0      | RFinger         | present_position
