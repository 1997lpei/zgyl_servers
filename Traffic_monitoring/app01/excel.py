import pandas as pd


def get_excel(file_path):
    """
    读取excel数据
    :param file_path:
    :return:
    """
    df = pd.read_excel(file_path)
    data = df.ix[:2000].values
    return data









if __name__ == '__main__':
    # get_excel()
    pass

