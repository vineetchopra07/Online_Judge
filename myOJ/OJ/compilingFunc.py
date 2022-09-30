import filecmp
from socket import timeout
import subprocess
from subprocess import PIPE, Popen
import os
from .models import Test_cases
# def compiler(code,testcases):
#     with open('/Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/solution.cpp', 'w') as f:
#         f.write(code)
#     os.system('g++ /Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/solution.cpp')
#     os.system('./a.out </Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/input.txt> /Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/output.txt')
#     # output1 = '/Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/input.txt'
#     # output2 = '/Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/output.txt'
#     user_output = open("/Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/output.txt","r")
#     original_output = open("/Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/original_output.txt","r")
#     out1 = user_output.readline()
#     out2 = original_output.readline()
#     ## close files
#     return out1 == out2



# def compiler(code,problemId):
#     OJ_input = Test_cases.objects.get(probId= problemId).input
#     output = Test_cases.objects.get(probId= problemId).output
#     file1 = open(r'/Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/sample.cpp','w')
#     file1.write(code)
#     file1.close()
#     print(input)
#     compile_com ="g++ /Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/sample.cpp -o /Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/output.exe"
#     run_com = "/Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/output.exe"
    # try:
    #     subprocess.run(compile_com,shell=True,check=True,timeout=3)
    #     try:
    #         op = subprocess(run_com,input=OJ_input,capture_output=True,check=True,timeout=1,text=True)
    #         cur_op = op.stdout.strip()
    #         print(cur_op)
    #     except subprocess.SubprocessErroras e:
    #         print(e.returncode)


    # return "AC"

def compiler(code,problemId):
    OJ_input = Test_cases.objects.get(probId= problemId).input
    output = Test_cases.objects.get(probId= problemId).output
    file1 = open(r'/Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/sample.cpp','w')
    file1.write(code)
    file1.close()
    verdirct = "AC"
    data, temp = os.pipe()
    os.write(temp, bytes(OJ_input, "utf-8"));
    os.close(temp)
    try:
        s = subprocess.check_output("g++ /Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/sample.cpp -o out2;./out2", stdin = data, shell = True).decode("utf-8")
        # user_output = s.decode("utf-8")
        print(s)
        # curr_op = s.stdout.strip()
        curr_op = ' '.join(s.splitlines())
        print(curr_op)
    except Exception as e:
        print('a')
        print(e)
        print(e.output)
        return "WA"
    
    print(output)
    if(s != output):
        verdirct="WA"

    print(verdirct)
    return verdirct

        