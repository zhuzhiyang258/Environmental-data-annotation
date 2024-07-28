# [English](#english-version) | [中文](#中文版本)

## <a name="中文版本"></a>描述
这是一个利用大模型，对文本中与环保相关的词条进行标注的demo。

## 使用方法

### 第一步：创建一个虚拟环境
```bash
conda create -n envproject python=3.10
conda activate envproject
```

### 第二步：安装依赖包
```bash
conda activate envproject
pip install -r requirements.txt
```

### 第三步：配置好环境变量
你需要配置好 `.env` 文件的环境变量，获取方式是通过豆包模型的官网进行获取(记得把example后缀去掉)。

### 第四步：运行脚本
```bash
python data_processor_untils.py
```

## 注意
这是一个不完整的项目，在处理大批量数据的逻辑上还存在一些缺陷，只能用来作为测试的最初版本。

---

## <a name="english-version"></a>Description
This is a demo that uses large models to annotate environmental terms in the text.

## Usage

### Step 1: Create a virtual environment
```bash
conda create -n envproject python=3.10
conda activate envproject
```

### Step 2: Install dependencies
```bash
cd .\Environmental-data-annotation\
pip install -r requirements.txt
```

### Step 3: Configure environment variables
You need to configure the environment variables in the `.env` file. You can obtain these from the Doubao Model's official website(Remember to remove the Example suffix).

### Step 4: Run the script
```bash
python data_processor_untils.py
```

## Note
This is an incomplete project, and there are some flaws in handling large volumes of data. It is only meant as an initial version for testing purposes.
