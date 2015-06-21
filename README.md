## dataset ##
you can download handwriting dataset from http://gorillamatrix.com/files/nist-sd19.rar

## run ##
- 写一个单词并保存
- 修改OneWordSolve.py下第92行，将其修改为你待测单词的路径
- 运行OneWordSolve.py

## 文件说明 ##

- data/handwritingDataX.pkl :  svm训练保存的结果
- calFeature.py :用于提取特征来训练svm
- correctWord.py:使用编辑距离进行单词的纠错
- myDic：   字典，用于单词的纠错
- OneCharacterRecognize.py :单个字母的识别
- OneWordSolve.py:  单个单词的识别
- Train_singleCharacter.py 单个字母准确率测试