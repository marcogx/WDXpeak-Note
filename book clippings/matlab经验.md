#  

本人接触matlab已经有5年多的时间了，一直想写点东西，但是之前不知道放在哪里才能发挥它的最大作用，直到几天前碰上了这个论坛（有点像诸葛亮遇见姜维，哈哈）
。  
  
废话不说，我想借贵论坛宝地，写一些经验给使用matlab的新手们，当然了，老大们也可以看看，不嫌弃我写得粗糙的话还可以指点一下，先谢过了～～～～  
  
首先我想说的是，matlab跟其他语言不一样（我用的比较多的编程语言，除了matlab就应该是c或c＋＋了，VB和Delphi也接触过，我想版面(matla
b版)大部分人也差不多），如果你抱着“把其他语言的思想运用在matlab里面”的话，那么我想，即使程序运行不出错，也很难把握matlab的精髓，也就很难发挥
matlab的作用了。所以，如果你是希望matlab作为VC的附属品，即你不想在matlab上面花太多功夫，只纯粹想用matlab来完成VC做不了或很难做成
的任务的话，那么，这篇文章你也不需要再阅读下去了；如果你是希望掌握一门语言、一个工具，使它更有效为你服务的话，那么，希望本文对你有所帮助。  
  
Matlab是一个基于矩阵运算的软件，这恐怕是众所周知的事情了，但是，真正在运用的时候（就是在编程的时候），许多人（特别是初学者）往往没有注意到这个问题，因
此，for循环（包括while循环）满天飞…………..这不仅是暴殄天物（没有发挥matlab所长），还浪费了你宝贵的时间。对此，版友MVH在他的“MATLA
B 小技巧”一文中也有所涉及，雷同的东西我也就不重复了，matlab的“帮助”里面也有相关的指示。我这里想说的一点是，初学者往往在初始化矩阵的时候注意到这个
问题，懂得了使用矩阵而不是循环来赋值，但是，在其他环节上，就很容易疏忽，或者说，仍然没有摆脱C＋＋的思想。举个例子吧，下面的代码是我的一个师弟写的，我想他接
触matlab也有2、3年时间了（在此说明一下，接触2、3年并不是表示每天都会跟matlab打交道，我本人也不是，只是在一年某几个时间段里面连续使用），但是
仍然会出现类似的问题：

  1. lt = size(imf1,2);
  2. for (i = 1:lt)
  3. if (abs(imf1(i)) > 1)
  4. break

上面的代码实现了一个目的――检查信号imf1（一个向量）是否存在绝对值大于1的点，这显然是基于C＋＋的思想写出来的。如果在matlab下面，其实用两个语句就
足够了（当然，可以合并为一个）：

  1. q = find(imf1>1);
  2. J = ~isempty(q);
_复制代码_

这样的修改带来的好处是很可观的。又如：

  1. for j = 1:num
  2. imf1(start1+j) = 2*li1(j+1) - imf1(start1+j);
_复制代码_

这是一个对称翻折的问题，它完全可以用以下这个语句简洁表示：

  1. imf1(start1+1:start1+num) = 2*li1(2:num+1) - imf1(start1+1:start1+num);

因此，如果是新手，可以先用循环（基于C＋＋的思想）来编写代码，然后看看能否用matlab的语言（基于矩阵的思想）来改进。当然，这样做的前提是你对matlab
提供的一些函数比较熟悉才行，这些函数在matlab的“帮助”那里搜索“Functions Used in
Vectorizing”就可以找到一些，其他的也可以找相关的书籍（没找到？不可能，电子版总可以下载到的）!  
对提高matlab编程能力的方法，我想主要有以下三个：

  1. 1\. 查help
  2. 2\. 多上上论坛，搜索帖子、发帖子问人
  3. 3\. 阅读别人、特别是牛人的程序
  4. 当然了，正如所有的程序语言一样，“3分课本7分上机”，一定要动手才行，不能光看。多想、多思考、多尝试，才是正路。

最后，整理一下常用的快捷键（用【】表示）或命令：

  1. 1\. 在命令窗口(Command Window)中：
  2. 1) 【上、下键】――切换到之前、之后的命令，可以重复按多次来达到你想要的命令
  3. 2) clc――清除命令窗口显示的语句，此命令并不清空当前工作区的变量，仅仅是把屏幕上显示出来的语句清除掉
  4. 3) clear――这个才是清空当前工作区的变量命令，常用语句clear all来完成
  5. 4) 【Tab】键――（转自版友心灯）在matlab@hit.edu.cn看到的：在command窗口，输入一个命令的前几个字符，然后按tab键，会弹出前面含这几个字符的所有命令，找到你要的命令，回车，就可以自动完成。目前讨论结果是：matlab6.5版本中，如果候选命令超过100个，则不显示。而在matlab7以后版本中，则没有这个限制，均可正常提示
  6. 5) 【Ctrl+C】（或【Ctrl＋Break】）――（转自版友yangjin_ren）在matlab程序运行过程中，可能由于程序编写的失误，导致程序不停的运行，在命令窗口输入“Ctrl+C”可以将运行的程序停下来，而不需要将整个Matlab程序关掉。不过进行此操作的前提是能够激活切换到命令窗口才行，呵呵。

2\. 在编辑器(Editor)中：

  1. 1) 【Tab】（或【Ctrl+]】）――增加缩进（对多行有效）
  2. 2) 【Ctrl+[】－－减少缩进（对多行有效）
  3. 3) 【Ctrl+I】－－自动缩进（即自动排版，对多行有效）
  4. 4) 【Ctrl+R】――注释（对多行有效）
  5. 5) 【Ctrl+T】――去掉注释（对多行有效）
  6. 6) 【Ctrl+B】――括号配对检查（对版本6.5有效，但版本7.0无效，不知道是取消了还是换了另外的快捷键，请大牛们指点，其他版本没有测试过）
  7. 7) 【F12】――设置或取消断点
  8. 8) 【F5】――运行程序
其余的例如在Debug状态下的快捷键就不多说了，自己看菜单Debug吧!  
  
累了， 有时间再写吧。希望大家多交流～～～～～～  
  
Coming: （以下东西都是一年前做的了，不知道能否记起，呵呵）

  1. 1) 关于神经网络的――调用matlab的nntool命令后的使用问题（我做的时候没有看过其他书籍或资料，是自己闭门造车的结果，如果写之前发现其他书籍有相关介绍的话就不写了）
  2. 2) 关于外部接口的――matlab与C＋＋Builder的接口，想详细介绍如何利用matcom 4.5在C++Builder中调用matlab的代码以及matcom的一些技巧。由于我不是搞项目开发的（搞科研、搞课题的），所以对VC不熟悉，大学的时候学过一点，不过我想对于搞科研来说C＋＋Builder就足够了，免去很多麻烦，Builder在界面设计和数据库连接上面（我只接触过这两方面）还是做得不错的。同样，如果发现其他书籍上有类似的东西就不写了
  3. 3) GUI方面也写写吧，只是一点点心得或者体会，呵呵，这个相对简单些，篇幅相对要少些。

真正接触matlab一年左右，我很喜欢上了matlab的简单的语法,易于绘制图形,gui编程也非常容易, 并且功能强大的开放式的toolbox。
因此,尽管我一直没有这方面的应用,但是我还是对它非常感兴趣。
现将个人的matlab的一点学习体会列在这里,愿能够对大家(特别是初学者)起到一点儿微薄的作用也好。

要说体会，我可以总结以下几条：  
1． 多动手写程序、调试  
2． 善于利用MATLAB的帮助  
3． 善于向别人学习  
4． 时间积累  
  
**＊多动手写程序、调试  
** 如果懒得写程序，调试程序，永远无法提高。我个人认为调试程序更重要。有些朋友可能在一个程序调试几下出不了结果时，就可能喜欢去问别人，我不太赞同这一做法。其实，凡事往往经过痛苦折磨后，才会让你印象深刻，收益更大。我建议在你觉得用尽你努力后，仍然无法有结果时，才去请教别人。我当初一个程序调试过一两个星期都有过。在这论坛上，你可以发现不少好的问题，对这些问题，不要光看别人如果解决，也不要光想怎么解决，自己坐下来，动手自己解决一下，那你就会把不是你的知识变成自己的知识。  
  
**＊善于利用MATLAB的帮助**  
可以这么说，任何问题都可以在MATLAB的帮助里找到解决的办法。问题不论大小，都是由更小的问题组成，把大问题化为小问题，小函数，然后再到MATLAB帮助里去
找这种小问题，小函数的用法。说实话，MATLAB里的函数太多，我也经常忘记一些用法，这时HELP就帮忙了。  
  
**＊善于向别人学习**  
在你解决一个问题后，你可能会发现别人有更简便的方法解决，更强的函数，就时就是你向别人学习的时候。说实话，在这论坛上，我也向bzzz,
bainhome等学习借鉴不少。  
  
**＊时间积累**  
时间长了，积累多了，当然也就有进步了。呵呵，也许再过几年，你会发现原来问题也不是以前想的那么难。而lyrock在这里发的也是“打糊乱说，小儿科”，那时你就已
经积累不少了。  
  
**1\. help:最有效的命令**（参阅了瀚海mathtools的 starrynight网友的文章）  
  
其实,可以这样说吧,如果离开matlab软件,我想我自己是基本上什么都不会。 一遇到什么问题,通常我的第一反应是:help
，就先说说自己对help的一些常用方法吧。  
1）命令窗口直接敲“help”，你就可以得到本地机器上matlab的基本的帮助信息。  
2）对于某些不是很明确的命令，只知道大体所属范围，譬如说某个工具箱，直接在命令窗口中敲入help
toolboxname，一帮可以得到本工具箱有关的信息：版本号，函数名等。  
3）知道函数名，直接用help funname就可以得到相应的帮助信息。  
  
**2\. see also：**不可小瞧的关联  
  
在用help命令的时候，可能因为我们开始估计的方向不一定完全正确，在列出的帮助信息中没有直接给出的我们要找的东西，但是我们一定不要忽略了在帮助的最后列出的s
ee also。  
譬如：曾经遇到一个画椭球的问题。刚开始我以为这个命令函数应该在graph3d中给出的（顺带提一句，只用help的时候我们就可以看到matlab\graph3
d - Three dimensional graphs. 。于是乎，我又help graph3d，很遗憾，在 Elementary 3-D
plots.中我没有发现画椭球的函数，但是我发现在see also中有SPECGRAPH. 抱着试试的态度，我又help specgraph，^_^，这次在
Solid modeling 中找到了ellipsoid - Generate ellipsoid。  
  
**3\. lookfor:** matlab中的google  
  
当我们很多什么头绪都没有的时候,我们可以求助于它，往往会收到意想不到的效果。  
譬如：曾经在gui编程的时候，遇到过这样一个问题：想拖动鼠标时，要出现一个方框，就像你在桌面上拖动鼠标，会出现虚线框一样。
当初我也刚开始一定都不知道该查找什么东西，后来想起用它了。于是乎，>> lookfor Rectangle
（很不好意思，当时这个矩形我还是在金山词霸中搞定的-_-）。果然，在其中就找到这样一条信息：GETRECT Select rectangle with
mouse.^_^  
  
**4\. get,set:** GUI object 属性的帮手  
  
在GUI编程中，我们可能有时候想改变某些object的属性，或者想让它安装自己的想法实现，但是我们又不记得这些object的属性，更别提怎么设置他们的值了。
这时，可以用 get（handles）得到此对象的所有的属及其当前值。用set（handles）可以得到对象所有可以设置的属性及其可能的取值。找到我们需要的
属性名字和可能的取值之后，就意义用 get（handles，‘propertyname’）取得此属性的值，用set（handles，‘propertynam
e’，values）设置此对象此属性的值。  
  
**5\. Edit：**查看m源文件的助手  
  
在应用matlab过程中，可能我们想看看它的m源文件，当然用editor定位打开也行，但是我经常采用的式直接在command窗口中用edit
funname.m，就省去了定位的麻烦。  
  
**6\. 其他常用命令：**which，what等  
  
which：定位指定的函数和文件，最好带上参数－all，以便显示更加多的信息  
what： 获得指定目录的m文件，mex文件以及mat文件名列表  
  
**7\. 各个高校bbs的mathtools版**  
  
谁都不可能什么都懂,但是永远记住这样一句话:Two heads are better than one.
多向他人请教，多相互讨论，这不只是在于解决matlab的问题上。  
我最经常去的bbs有:  
.瀚海星云(<http://fbbs.ustc.edu.cn/>的mathtools版  
.水木清华(<http://www.smth.edu.cn/ver2.html>的mathtools版  
.饮水思源(<http://bbs.sjtu.edu.cn/>的mathtools版  
.紫丁香 (<http://bbs.hit.edu.cn/>的matlab版  
  
**8\. 一些专业网站**  
  
我所知道的有:  
1) [http://www.mathworks.com](http://www.mathworks.com/) mathworks的官方网站  
2) <http://www.mathtools.net/MATLAB/index.html>
这里有很多好的工具箱或者小的辅助函数可以下载,不过是国外的,e文和网络对来说感觉都是很不爽的事情。  
3) <http://matlab.myrice.com/>
Matlab大观园，估计只要在网上搜索过matlab资料的就不会不知道它，园主是东北大学的薛定宇教授，一直从事MATLAB语言及其应用研究。  
4) <http://passmatlab.myetang.com/MATLAB/INDEX.HTM>文宇工作室  
5) <http://sh.netsh.com/bbs/5186/> matlab语言与应用，薛定宇的一个论坛  
6)
<http://www.matwav.com/resource/newlk.asp>中国学术交流园地，除了matlab有关外，还有很多其他的专业的文章。  
  
**最后一条，要大胆的去试，哪怕只有一丁点儿可能。  
**  
譬如，早些时候，有朋友问我：我用什么命令可以查找所建立网络的属性的含义，比如说：我建立网络  
net=newff(minmax(p),[3,1], {'tansig','purelin'},'traingda');  
想看看net.trainParam。lr_inc属性是啥含义用什么命令查看呢？  
当时，我根本连练习都没有用matlab的神经网络工具箱的东西练习过。我helpnewff也没有结果，后来实在没有办法，就试着help参数值traingda，
没有想到还居然真的就找到答案了。  
还有，曾经有朋友想把waitbar的默认颜色的红色改掉，我用help 没有发现可以改变其填充色的property，后来我看了waitbar.m，发现其填充色
本来就不试一个可变参数，但是既然发现了是什么地方，就可以自己改变的，这都得益于matlab
的开放性。这也为我们提供了很大的灵活性（在他的基础上，我们可以做很少的变换，就自己写一个填充色可以以属性输入而改变的waitbar的）。  
  
**最后，**matlab只是一个很好的应用工具而已，也不像vc，delphi，vb等开发工具，最多的还是应用于算法的验证，仿真等。我们应该的是尽可能的知道一点儿基础的，然后熟悉本专业的toolbox。（可惜，我现在一直没有这样的实际应用机会）

  

