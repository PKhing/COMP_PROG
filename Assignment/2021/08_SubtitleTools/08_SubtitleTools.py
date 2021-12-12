# Subtitle Tools
# Your ID

# ------------------------------------------
def read_file(file_name):
    data=[]
    inputFile =  open("Assignment/2021/08_SubtitleTools/"+file_name , encoding='utf-8')
   
    for line in inputFile.read().strip().split('\n\n'):
        x = line.split('\n')
        time = x[1].replace('\n','').split(' --> ')
        data.append([time_string_to_number(time[0]),time_string_to_number(time[1]),"\n".join(x[2:])])
    inputFile.close()
    return data

def write_file(file_name,data):
    outputFile = open("Assignment/2021/08_SubtitleTools/"+file_name, "w", encoding='utf-8')
    for i in range(len(data)):
        outputFile.write(str(i+1)+'\n')
        timest,timeed,text = data[i]
        outputFile.write(time_number_to_string(timest)+' --> '+time_number_to_string(timeed)+'\n')
        outputFile.write(text+'\n')
        outputFile.write('\n')
    outputFile.close()

def time_string_to_number(time_str):
    number = 0
    hour,minute,second = time_str.split(':')
    second,ms = second.split(',')
    number+= int(ms)+int(second)*1000+int(minute)*60*1000+int(hour)*60*60*1000
    return number

def time_number_to_string(time_number):
    hour = time_number//(60*60*1000)
    time_number%=60*60*1000
    minute = time_number//(60*1000)
    time_number%=60*1000
    second = time_number//(1000)
    time_number%=1000
    ms = time_number
    return str(hour).zfill(2)+':'+str(minute).zfill(2)+':'+str(second).zfill(2)+','+str(ms).zfill(3)

# -----------------------------------------
def shift(file_in, time_shift, file_out):
    data = read_file(file_in)
    newData = []
    for [sttime,edtime,text] in data:
        sttime= max(sttime+time_shift,0)
        edtime=max(edtime+time_shift,0)
        if sttime>0 or edtime>0:
            newData.append([sttime,edtime,text])

    write_file(file_out, newData)

# ------------------------------------------
def find_min_diff(startTime,data):
    idx = 0
    mn = abs(data[0][0]-startTime)
    for i in range(len(data)):
        if abs(data[i][0]-startTime)<mn:
            mn = abs(data[i][0]-startTime)
            idx = i
    return idx,mn

def merge(base_file, merge_file, threshold, file_out):
    base_data = read_file(base_file)
    merge_data = read_file(merge_file)
    newData = []
    for [sttime,edtime,text] in merge_data:
        idx,diff = find_min_diff(sttime,base_data)
        if diff <= threshold:
            base_data[idx][2]+="\n"+text
        else:
            newData.append([sttime,edtime,text])
    newData+=base_data
    newData.sort()
    
    write_file(file_out, newData)

# ------------------------------------------
def remove_between(string,stchar,edchar):
    stidx = string.find(stchar)
    edidx = string.find(edchar)
    while stchar in string and edchar in string:
        stidx = string.find(stchar)
        edidx = string.find(edchar)
        string = string[:stidx]+string[edidx+1:]
    return string

def is_symbol_only(string):
    for x in string:
        if x.isalnum():
            return False
    return True

def remove_symbol_only(text):
    newText = []
    for line in text.split('\n'):
        if not is_symbol_only(line):
            newText.append(line)
    return '\n'.join(newText)

def clean(file_in, file_out):
    data = read_file(file_in)
    newData = []
    for [sttime,edtime,text] in data:
        text = remove_between(text, "(", ")")
        text = remove_between(text, "[", "]")
        text = remove_between(text, "<", ">")
        text = remove_between(text, "{", "}")
        text = remove_symbol_only(text)
        if text != "":
            newData.append([sttime,edtime,text])
    write_file(file_out, newData)


# ------------------------------------------

# shift('test.srt', -5500, 'test1_shifted.srt')

# merge("test2_en.srt", "test2_th.srt", 1000, "test2_merged.srt")

clean('test3_th.srt', 'test3_th_cleaned.srt') 