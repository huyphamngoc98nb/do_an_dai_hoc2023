import os
import scipy.io
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import traceback
# Thư mục chứa các tệp MAT
directory = "/đường_dẫn_đến_thư_mục"
directory = os.path.dirname(os.path.abspath(__file__))

def case_1():
    try:
        directory = os.path.dirname(os.path.abspath(__file__))
        folder_name = "src\AUROCMaterialDrawChart"
        directory = os.path.join(directory, folder_name)
        # Lấy danh sách tất cả các tệp MAT trong thư mục
        mat_files = [f for f in os.listdir(directory) if f.endswith(".mat")]

        # Tìm tên file lớn nhất dựa trên thời gian tạo
        if mat_files:
            latest_file = max(mat_files)
            latest_file_path = os.path.join(directory, latest_file)

            # Đọc dữ liệu từ tệp MAT
            data = scipy.io.loadmat(latest_file_path)

            # Trích xuất FPR và TPR từ dữ liệu
            fpr = data['FPR'].reshape(-1)
            tpr = data['TPR'].reshape(-1)

            roc_auc = metrics.auc(fpr, tpr)

            # Vẽ biểu đồ ROC Curve
            plt.figure()
            plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.5f)' % roc_auc)
            plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Biểu đồ ROC')
            plt.legend(loc='lower right')
            plt.show()
        else:
            print("Không tìm thấy tệp MAT trong thư mục.")
    except Exception:
        traceback.print_exc()
def case_2():
    try:
        directory = os.path.dirname(os.path.abspath(__file__))
        folder_name = "src\AUPRMaterialDrawChart"
        directory = os.path.join(directory, folder_name)
        # Lấy danh sách tất cả các tệp MAT trong thư mục
        mat_files = [f for f in os.listdir(directory) if f.endswith(".mat")]

        # Tìm tên file lớn nhất dựa trên thời gian tạo
        if mat_files:
            latest_file = max(mat_files)
            latest_file_path = os.path.join(directory, latest_file)

            # Đọc dữ liệu từ tệp MAT
            data = scipy.io.loadmat(latest_file_path)

            # Trích xuất FPR và TPR từ dữ liệu
            recall = data['Recall'].reshape(-1)
            precision = data['Precision'].reshape(-1)

            roc_aupr = metrics.auc(recall, precision)

            # Vẽ biểu đồ AUPR Curve
            plt.figure()
            plt.plot(recall, precision, color='darkorange', lw=2, label='AUPR curve (area = %0.5f)' % roc_aupr)
            plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('Recall')
            plt.ylabel('Precision')
            plt.title('Biểu đồ AUPR')
            plt.legend(loc='lower right')
            plt.show()
        else:
            print("Không tìm thấy tệp MAT trong thư mục.")
    except Exception:
        traceback.print_exc()

# Tạo một từ điển ánh xạ giữa giá trị đầu vào và các hàm tương ứng
cases = {
    1: case_1,
    2: case_2
}

# Nhập giá trị từ bàn phím
try:
    choice = int(input("Nhập số để vẽ biểu đồ: 1 - ROC; 2 - AUPR: "))
    # Kiểm tra xem giá trị đã nhập có trong từ điển không
    if choice in cases:
        # Gọi hàm tương ứng với giá trị đã nhập
        cases[choice]()
    else:
        print("Không tìm thấy trường hợp phù hợp.")
except ValueError:
    print("Vui lòng nhập một số nguyên từ 1 đến 2.")
