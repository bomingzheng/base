//js单行注释  /*多行注释*/
// 变量，需要声明
// 变量命名规则使用短名称见名知意，必须以字母开头，可以用￥和_开头但是不推荐，由字母和数字组成遵循驼峰原则，大小写敏感

var name = '露娜';                //先声明在赋值
var age;                        //只声明不赋值,只声明不赋值会返回一个undefined
age = 18;                          //声明后可以直接赋值
var a =10, b=15, c=25;           // 多个变量赋值
dent = 20;                         // 不声明直接赋值，它不报错会变成windows的一个属性
alert(window.dent);              // 弹窗显示，通过window.属性获取值
console.log(age);              //输出到控制台


// 数据类型： 数字，字符串，Allay，null，undefined boolean
// js是一门弱类型的语言,通过 var、let定义变量，const定义常量

//数字类型
var x=12;
var y=1.3;

// 字符串，常量
const z = 'asw';

// 数组和Allay属性
var list = Array(1, 2, 3, 4, 5);   //Allay:相当于python的列表可通过下标取值
console.log(list.length);               // .length 返回数组的元素长度
console.log(list.push("b", 7))          // .push方法：向数组插入元素，最后位置
console.log(list.pop())                 // .pop方法：获取出数组中最后一个元素删除

//定义一个空类型有值
let d =null;

// undefined 变量已声明，未赋值
let e;

//  boolean   类型：true false （小写）
var f = true;
var g = false;

// 运算符
//   == (判断只比较内容不比较类型)  ===（判断比较内容类型都匹配才成立）  &&(与)   ||(或)   !（非）
//  ++和+=作用是一样的都是+1（ 在控制台返回值不一样：++ 先打印变量值，+运算、  += 直接+运算赋值输出）

// 条件语句
var h =5;
if(h>5){
console.log("条件太大");}
else if(h===5){
    console.log("条件成立")
}
else{
    console.log("条件太小");
}

// switch 语句
let i =3,j=7;
switch (j-i) {
    case 3:
        console.log("欢迎光临");
        break;
    case 4:{
        console.log("恭喜发财");
        break;      //不写break匹配上，还会继续匹配
    }
     default:   // 上面选项未匹配，执行默认代码
        console.log("上面选项未匹配，执行默认代码")
}
// 函数
// 无参数
function f1() {
    console.log("执行自定义的函数");
}
// 有参数函数

function add(a,b) {
   let k =(a + b);
     return b-a    //函数没有返回值，返回undefined，有返回值需要用变量接收
}
l =add(11,7);
console.log(l)

//对象
// 创建对象两种方式：objA=new objA();   var objA={};
// 对象属性key不用引号引起来，属性可以创建时设定也可以动态添加
// 操作对象属性： objA.name   objA["name"]   调用对象方法 objA.fs();
 var objA = {
    name:"孙悟空",
     fs:function (a,b) {        //对象里面创建方法，不需要填写方法名
        return b -a;
     }
 };

// 循环
// while 条件循环
var m =0;
while (m < 5){
    console.log(m)
    m++;
}

//for 循环(语句1循环开始前执行，语句2循环的条件，语句3每一轮循环结束执行)
for (var n =6; n<10; n++){
    console.log(n)
}

// for in:遍历循环，比如数组、字典
var alist=Array(1,3,5,7,9);
for(i in alist){
    console.log(i)   // 遍历出来的是数组的下标
    console.log(alist[0])   //通过下标遍历数组的值
}
var skips ={
    name:"小米",
    age:18,
    sex:"nan"
}
for (i in skips){
    // console.log(i)  //遍历出来的是对象的key
     console.log(skips[i])   // 通过字典的key来获取值
}