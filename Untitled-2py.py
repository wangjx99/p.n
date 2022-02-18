import os

if __name__ == '__main__':
    # n = 0
    # with open("E:/cmip6_d/url_total.txt", 'r') as fr:  # 读取所有下载链接信息
    #     for line in fr.readlines():  # 按行读取
    #         n += 1
    # print(n)

    fw = open("E:/cmip6_d/url_nodup.txt", 'w')
    name = []
    with open("E:/cmip6_d/url_total.txt", 'r') as fr:  # 读取所有下载链接信息
        for line in fr.readlines():  # 按行读取
            basename = os.path.basename(line)
            if basename not in name:
                name += [basename]
                fw.write(line)
