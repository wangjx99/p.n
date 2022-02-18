import re

if __name__ == '__main__':
    fw = open("E:/cmip6_d/url_total.txt", 'a')  # 创建url保存文件
    with open("E:/cmip6_d/wget-20220121142120.sh", 'r') as fr:  # 读取所有下载链接信息
        for line in fr.readlines():  # 按行读取
            print(line)
            # line = line.strip('\n').split(' ')  # 去掉换行符并分割
            match = str(re.findall(r"'http://.*.nc'", line)) # 清洗并获取待下载地址
            if len(match) > 2:
                fw.write(match[3:-3] + '\n')  # 将下载地址写入保存文件中
    fw.close()  # 关闭文件
