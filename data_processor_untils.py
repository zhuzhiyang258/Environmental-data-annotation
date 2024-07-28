import pandas as pd
from label_utils import LabelUtils

class DataPreprocessor:
    def __init__(self, excel_path, chunk_size=20, debug=True):
        self.excel_path = excel_path  # Excel文件路径
        self.chunk_size = chunk_size  # 每块的大小
        self.debug = debug  # 调试模式标志
        self.df = pd.read_excel(excel_path)  # 读取Excel文件
        if self.debug:
            print(f"Excel文件已读取，共有 {len(self.df)} 行数据。")
        self.seventh_column_df = pd.DataFrame(self.df.iloc[:, 6].values, columns=['rowtext'])  # 提取第七列数据
        if self.debug:
            print(f"第七列数据已提取，共有 {len(self.seventh_column_df)} 行数据。")
        self.processed_data = pd.DataFrame(columns=['rowtext', 'labeledtext'])  # 初始化处理后的数据
        self.chunk_counter = 0  # 块计数器
        self.file_counter = 1  # 文件计数器
        self.label_utils = LabelUtils()  # 初始化标签工具

    def chunked_iterator(self):
        """定义一个迭代器函数，每次输出指定大小的块"""
        for start in range(0, len(self.seventh_column_df), self.chunk_size):
            yield self.seventh_column_df[start:start + self.chunk_size]

    def process_chunk(self, chunk, i):
        """处理单个块的逻辑"""
        if self.debug:
            print(f'正在处理第 {i + 1} 个块')  # 输出当前处理的块编号
            print(chunk)  # 输出当前处理的块内容
        
        try:
            chunk['labeledtext'] = chunk['rowtext'].apply(self.label_utils.label)  # 对整个块应用标注
        except Exception as e:
            print(f"标注第 {i + 1} 个块时出错: {e}")
            return

        # 将标注后的行追加到 processed_data DataFrame 中
        self.processed_data = pd.concat([self.processed_data, chunk], ignore_index=True)
        self.chunk_counter += 1

        # 每处理5个块，保存到当前文件
        if self.chunk_counter % 5 == 0:
            current_excel_path = f'test_{self.file_counter}.xlsx'
            self.save_to_excel(current_excel_path)
            if self.debug:
                print(f'处理 {self.chunk_counter} 个块后保存到 {current_excel_path}')

    def save_to_excel(self, path):
        """保存 processed_data 到指定路径的 Excel 文件"""
        self.processed_data.to_excel(path, index=False)
        if self.debug:
            print(f"数据已保存到 {path}")

    def run_labeling(self):
        """运行数据预处理"""
        iterator = self.chunked_iterator()
        for i, chunk in enumerate(iterator):
            self.process_chunk(chunk, i)

        # 处理最后一个不足chunk_size的块
        if not self.processed_data.empty:
            final_excel_path = f'test_{self.file_counter}.xlsx'
            self.save_to_excel(final_excel_path)
            if self.debug:
                print(f'处理完所有块后保存到 {final_excel_path}')

# 使用示例
preprocessor = DataPreprocessor('test.xlsx')
preprocessor.run_labeling()
