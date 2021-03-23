// 单行注释: 以//开头
// 多行注释: 以/*    以*/结

// 变量  需要先声明： 先声明在赋值  同时声明在赋值  只声明不赋值
/*
var、let、const 区别？
    const声明:   其作用是声明常量的
    var声明:     在函数内用var声明的变量作用仅在这个函数内，而对函数外部是不作用的

 */
let name;       // 只声明不赋值
let age = 18;   // 声明并赋值
name = '莉莉';  //  先声明在赋值
        // 在浏览器的console控制台调试js代码
        /*
        defined: 声明了变量没有赋值或者变量提升了。
        变量提升=用var声明的变量可以在声明之前使用，值为undefined
        */
alert(name);       //进入页面弹框展示该变量的值
console.log(age);  //控制台输出该变量的值
gender = '亢龙有悔';   // 不声明会变成window的一个属性
alert(window.gender);
/* 命名规则：
    驼峰命名
    必须用字母开头
    可以使用$和_以这两个符号开头的
    变量大小写敏感
 */

// 数据类型： 字符串、数组、数字类型、undefined、null、boolean
let a = 10, b = 11.22;
let s ='hello'
let c = Array(1,2,3,4,5);
// 数组属性
c.length;   // 返回数组的元素数量
c.push(1);   //向数组最后位置添加元素
c.pop();   // 获取数组最后的一个元素

let d=null;     //定义空类型，有值=null
let e;          //undefined类型已声明未赋值
let f = true;   //定义布尔类型，小写
let g = false;  // f===1  g===0 有数值等用true

/*
运算符：
+ - * / %
= += -= *= /= %= ++
== === > < >= <= !=
&&   ||  !

==只比较内容不比较类型  ===判断比较--内容和类型都匹配才成立
++是先打印变量值在做+运算   += 是先做+运作在输出  它们两个作用是相通的只是控制台返回值不同

*/

let h = 4;
if(h === 4){
    h= h-1;}
    else if(h<4){
        h = h+1;}
    else {
        h=0
}

let i=8;
    switch (i+1){
        case 7:
            console.log("今天是周一");
            break;
        case 4:
            console.log("今天周末");
            break;
        default:
            console.log("今天国庆节")
                //不写break 匹配上以后还会执行，上面选项都未匹配执行default的用例
    }

function DK(){
        console.log("不带参数的函数")
}
function add(a, b){
        return a+b
    //函数没有返回值返回undefined，有返回值需要变量接收
}

let obJa = {
        name: "悟空",
        KO:function (a, b){
            return b -a;
        }
        // 对象创建：obJA=new objA()  或者 let objA = {}

    // 对象属性不用引号，属性可以创建设定也可以东涛添加
    // obJA.name 或者 obJA["name"] 来操作属性 obJA.KO() 操作对象方法
}

let j =0;
    while (j<8){
        console.log(j);
        j++;
    }

