from PIL import Image

TOP2BOTTOM = 1
BOTTOM2TOP = -1
LEFT2RIGHT=2
RIGHT2LEFT=-2
RED=10
GREEN=20
BLUE=30
HUE=1
SAT=2
LUM=3
def abso(x):
    if (x<0):
        return -x
    return x
def sort(arr, sortby):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j][sortby] > arr[j+1][sortby]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main(source, dest, direction = LEFT2RIGHT, sortby=HUE):
    if (sortby == RED or sortby == GREEN or sortby == BLUE):
        flag = Image.open(source).convert("RGB")
        sortindex=sortby//10-1
    elif (sortby == HUE or sortby == SAT or sortby == LUM):
        flag = Image.open(source).convert("HSV")
        sortindex = sortby - 1
    else:
        assert("Invalid Sortby")
    if (direction == 0):
        assert ("Invalid Direction")
    elif (abso(direction) == 2):
        lineindex = 0
    elif (abso(direction) == 1):
        lineindex = 1
    else:
        assert("Invalid Direction")
    print(sortindex)
    print(lineindex)



    if (direction < 0):
        start, end = flag.size[lineindex], 0
    else:
        start, end = 0, flag.size[lineindex]

    flagdump = flag.load()
    print(flagdump[0,0])

    pixels=[]
    for i in range(start, end):
        pixels.append(flagdump[(1-lineindex)*i, lineindex*i])

    print (pixels)
    sort(pixels,sortindex)
    print (pixels)
    for y in range(flag.size[1-lineindex]):
        for i in range(len(pixels)):
            flagdump[abso(start-i)*(1-lineindex) + y*(lineindex), abso(start-i)*lineindex + y*(1-lineindex)]=pixels[i]
            print(str(y) + " " +  str(pixels[i]))
    flag.convert("RGB").save(dest)


main("D:\\Users\\Noam10\\Desktop\\pride_flag.png", "D:\\Users\\Noam10\\Desktop\\pride_flag sorted.png",  direction = TOP2BOTTOM, sortby=LUM)