import matplotlib.pyplot as plt
import cv2
import os
# 遍历 font 文件夹的文件
root = 'fontInput'
outroot = 'fontInput'
files = os.listdir(root)
# 除去文件夹
files = [file for file in files if not os.path.isdir(os.path.join(root, file))]
# 创建 fontBinarized 文件夹
if not os.path.exists(outroot):
    os.mkdir(outroot)


def basename(path):
    return os.path.basename(path).split('.')[0]


def extname(path):
    return '.' + '.'.join(os.path.basename(path).split('.')[1:])


fig, ax = plt.subplots(ncols=len(files), nrows=2)
# fig.dpi = 300
for i, file in enumerate(files):
    # 读取文件
    img = cv2.imread(os.path.join(root, file))
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    # 保存文件
    cv2.imwrite(os.path.join(
        outroot, f'{basename(file)}{extname(file)}'), binary
    )
    # 显示图片
    ax[0][i].imshow(img)
    ax[1][i].imshow(binary)

# 显示
plt.show()
