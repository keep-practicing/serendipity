# Data Structures

[![Build Status](https://travis-ci.org/zwfang/serendipity.svg?branch=master)](https://travis-ci.org/zwfang/serendipity)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/97bd89b51f684d3a8ebb9b1b93887665)](https://www.codacy.com/app/zwfang/serendipity?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=zwfang/serendipity&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/zwfang/serendipity/branch/master/graph/badge.svg)](https://codecov.io/gh/zwfang/serendipity)
[![](https://img.shields.io/badge/python-3.7-blue.svg?logo=appveyor&style=flat)](https://img.shields.io/badge/python-3.7-blue.svg?logo=appveyor&style=flat)

 > 数据结构是计算机中存储、组织数据的方式。
 > 
 > 数据结构意味着接口或封装：一个数据结构可被视为两个函数之间的接口，或者是由数据类型联合组成的存储内容的访问方法封装。


## 数据结构分类（逻辑分类）
1. 线性结构
    > 有且仅有一个开始和一个终端结点，并且所有结点都最多只有一个直接前趋和一个后继。 

    [数组](serendipity/linear_structures/array.py)、[单链表](serendipity/linear_structures/singly_linked_list.py)、[栈(底层结构为数组)](serendipity/linear_structures/array_stack.py)、[栈(底层结构为单链表)](serendipity/linear_structures/singly_linked_list_stack.py)、[队列(底层结构为数组)](serendipity/linear_structures/queue.py)、[循环队列(底层结构为数组)](serendipity/linear_structures/loop_queue.py)、[队列(底层结构为单链表)](serendipity/linear_structures/singly_linked_list_queue.py)

2. 非线性结构
    > 一个结点可能有多个直接前趋和直接后继。

    [二分搜索树](serendipity/tree_structures/bst.py)


*  数据结构应用

    [集合set(底层结构为二分搜索树)](serendipity/set_and_map/bst_set.py)、[集合set(底层结构为单链表)](serendipity/set_and_map/singly_linked_list_set.py)、[映射map(底层结构为单链表)](serendipity/set_and_map/singly_linked_list_map.py)、[映射map(底层结构为二分搜索树)](serendipity/set_and_map/bst_map.py)

## 笔记
[栈](docs/singly_linked_list_stack.md)、[队列](docs/singly_linked_list_queue.md)、[二分搜索树](docs/binary_search_tree.md)、[集合set](docs/set_time_complexity_analyse.md)、[映射map](docs/map_analyse.md)

## 数据存储结构---顺序存储、链接存储、索引存储、散列存储
>  顺序存储和链接存储适用在内存结构中。
> 
> 索引存储和散列存储适用在外存与内存交互结构。
1. 顺序存储

    顺序存储方式就是在一块连续的存储区域一个接着一个的存放数据。顺序存储方式把逻辑上相连的结点存储在物理位置上相邻的存储单元里。通常顺序存储结构是借助于计算机程序设计语言(例如，C/C++)的数组来描述。

    特点：
    1. 随机存取表中元素。
    2. 插入和删除操作需要移动元素。

2. 链接存储

    在计算机中用一组任意的存储单元存储数据元素(这组存储单元可以是连续的,也可以是不连续的)。它不要求逻辑上相邻的元素在物理位置上也相邻.因此它没有顺序存储结构所具有的弱点,但也同时失去了顺序表可随机存取的优点。结点间的逻辑关系是由附加的指针字段表示的。

    特点：
    1. 比顺序存储结构的存储密度小 (每个节点都由数据域和指针域组成，所以相同空间内假设全存满的话顺序比链式存储更多)。 
    2. 逻辑上相邻的节点物理上不必相邻。 
    3. 插入、删除灵活 (不必移动节点，只要改变节点中的指针)。 
    4. 查找结点时链式存储要比顺序存储慢。
    5. 每个结点是由数据域和指针域组成。

3. 索引存储

    除建立存储结点信息外，还建立附加的索引表来标识结点的地址。索引表由若干索引项组成。索引表中的每一项称为索引项，索引项的一般形式是关键字与地址。关键字唯一标识一个结点，地址作为指向结点的指针。带有索引表的存储结构可以大大提高数据查找速度。

    特点：
    * 索引存储结构是用结点的索引号来确定结点存储地址，其优点是检索速度快，缺点是增加了附加的索引表,会占用较多的存储空间。

4. 散列存储

    散列存储，又称hash存储，是一种力图将数据元素的存储位置与关键码之间建立确定对应关系的查找技术。
    散列法存储的基本思想是：由节点的关键码值决定节点的存储地址。散列技术除了可以用于查找外，还可以用于存储。

    特点：
    * 散列是数组存储方式的一种发展，相比数组，散列的数据访问速度要高于数组，因为可以依据存储数据的部分内容找到数据在数组中的存储位置，进而能够快速实现数据的访问，理想的散列访问速度是非常迅速的，而不像在数组中的遍历过程，采用存储数组中内容的部分元素作为映射函数的输入，映射函数的输出就是存储数据的位置，这样的访问速度就省去了遍历数组的实现，因此时间复杂度可以认为为O(1)，而数组遍历的时间复杂度为O(n)。

<br/>

***数据结构是指计算机处理的数据元素的组织形式和相互关系，数据类型是某种程序设计语言中已经实现的数据结构。抽象数据类型ADT是从问题的数学模型中抽象出来的逻辑数据结构和逻辑数据结构上的运算，而不考虑计算机的具体存储结构和运算的具体实现算法。***
