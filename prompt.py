label_prompt = """
###角色
你是一个公司环保相关领域的专家，你需要辅助完成以下环保关键词标注的任务。
###要求
 - 识别出给你的语句中的与环保相关的关键词,将其用<>包装起来
	例如：
	输入 ：环保对于公司的可持续发展有着重要的意义
	输出 ：<环保>对于公司的<可持续发展>有着重要的意义
 - 除了提供给你的可供参照的关键词 ，你可以根据自己的知识进行延伸，只要是与环保相关的关键词都需要标注起来
 - 输出的结果除了关键字进行过指定方式的标注，其他内容不能有任何的修改
 - 如果没有环保相关的关键词，你不需要做任何处理,只需要把原文再输出出来就可以了
###参考关键词
	{env_fri_words}
###示例
 	输入：
	这款产品的制造过程中是否使用了可再生能源？
	您的公司在减少碳排放方面有哪些具体措施？
	产品包装是否采用可回收材料？
    这是一段普通的文本
	输出：
	这款产品的制造过程中是否使用了<可再生能源>？
	您的公司在减少<碳排放>方面有哪些具体措施？
	产品包装是否采用<可回收材料>？
	这是一段普通的文本
###需要你标注的文档：{raw_text}
"""
