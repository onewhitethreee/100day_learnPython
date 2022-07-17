import argparse
parser = argparse.ArgumentParser(description='manual to this script')

# 第一个实参就是命令行等号左边的参数的名字
# 第二个实参是传入参数的类型
# 第三个实参是传入参数的默认值
parser.add_argument('--sentences', type=str, default=None)
parser.add_argument('--results', type=str, default=None)
args = parser.parse_args()
print (args.sentences)
print (args.results)