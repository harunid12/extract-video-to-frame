import cv2
import os

print('#'*40)
print('#'*8 + ' Extract Video to Frame ' + '#' * 8)
print('#'*8 + ' Create By: Ahmad Harun ' + '#'* 8)
print('#'*40)
print('')
# Read the video from specified path
nama_file = input('masukan nama file dan extension: ')
cam = cv2.VideoCapture(nama_file)
  
try:
      
    # creating a folder named data
    # if not os.path.exists('/py-ta/fix/hasil'):
    #     os.makedirs('/py-ta/hasil')
    folder = input('Masukan Alamat folder hasil extract : ')
    os.makedirs(folder)
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0
i = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        i += 1
        # if video is still left continue creating images
        # save frame
        name = folder + '/haki' + str(i) + '.jpg'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 30 # i.e. at 30 fps, this advances one second
        cam.set(1, currentframe)
    else:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()

print('')
print('Thank You!')

print('')
print('#'*40)
print('#'*8 + ' Extract Video to Frame ' + '#' * 8)
print('#'*8 + ' Create By: Ahmad Harun ' + '#'* 8)
print('#'*40)