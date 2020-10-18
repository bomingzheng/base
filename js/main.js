alert("欢迎来到js世界！ ");
//js单行注释  /*多行注释*/
// 变量，需要声明
// 变量命名规则使用短名称见名知意，必须以字母开头，可以用￥和_开头但是不推荐，由字母和数字组成遵循驼峰原则，大小写敏感

var name = '露娜';          //先声明在赋值
var age;                        //只声明不赋值,只声明不赋值会返回一个undefined
age=18;                          //声明后可以直接赋值
dent=20;                         // 不声明，直接赋值他不报错会变成windows的一个属性
alert(window.dent);
alert(name);                    // 弹窗显示
console.log(name);              //输出到控制台
var a =10, b=15, c=25;           // 多个变量赋值

// 数据类型： 数字，字符串，Allay，null，undefined boolean
// js是一门弱类型的语言
var a=12;    //数字类型
var b=1.3;  //数字类型
var t='asw';   // 字符串
var list=Array(1,2,3,4,5);   //Allay:相当于python的列表可通过下标取值
// Allay属性
// .length 返回数组的元素长度
// .push方法：向数组插入元素，最后位置
// .pop方法：从数组最后位置取数据
var c =null;   //定义一个空类型有值，undefined是只声明没赋值
var d = true;  //true和相等
var e = false;   //boolean  类型只有true和false 小写
// 运算符   == (只比较内容是不是相等)，===（不光内容相同，并且还要是一种数据类型）  &&(与)   ||(或)   !（非）
// ++ 先打印在赋值+   += 直接相加赋值
// 条件语句
var f =5;
if(f>5){
alert("条件太大");}
else if(f===5){
    alert("条件成立")
}
else{
    alert("条件太小");
}
// switch 语句
var p =3,s=7;
switch (s-p) {
    case 3:
        console.log("欢迎光临");
    break;
    case 4:{
        console.log("恭喜发财");
        break;      //不写break匹配上，还会继续匹配
    }
    default:
        console.log("上面选项未匹配，执行默认代码")
}
// 定义函数
function f1() {
    console.log("执行自定义的函数");
}
function add(a,b) {
    s =(a + b);
    return s    //函数没有返回值，返回undefined
}
r =add(11,7);
console.log(r)

//对象
 var objA = {
    name:"孙悟空",
     fs:function (a,b) {
        return b -a;
     }
 };
// 操作对象属性： objA.name   objA["name"]   调用对象方法 objA.fs();

