<style>
pre {
 white-space: pre-wrap;
}
</style>

# Language-Model

基于 PyTorch [范例](https://github.com/pytorch/examples/tree/master/word_language_model) 实现中文语言模型。

## 数据集

《三国演义》 + 《三体》

## 模型

<pre>
RNNModel(
  (drop): Dropout(p=0.5)
  (encoder): Embedding(3719, 200)
  (rnn): GRU(200, 200, num_layers=2, dropout=0.5)
  (decoder): Linear(in_features=200, out_features=3719, bias=True)
)
</pre>

## 生成效果

### 《三国演义》

![image](https://github.com/foamliu/Language-Model/raw/master/images/result-1.PNG)

![image](https://github.com/foamliu/Language-Model/raw/master/images/result-2.PNG)

![image](https://github.com/foamliu/Language-Model/raw/master/images/result-3.PNG)

![image](https://github.com/foamliu/Language-Model/raw/master/images/result-4.PNG)

### 《三体》

![image](https://github.com/foamliu/Language-Model/raw/master/images/result-5.PNG)

![image](https://github.com/foamliu/Language-Model/raw/master/images/result-6.PNG)

![image](https://github.com/foamliu/Language-Model/raw/master/images/result-7.PNG)

![image](https://github.com/foamliu/Language-Model/raw/master/images/result-8.PNG)

![image](https://github.com/foamliu/Language-Model/raw/master/images/result-9.PNG)



