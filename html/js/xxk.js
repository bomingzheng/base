$(function () {
    //添加参数行
    $(".add_head").click(function () {
        // 获取参数行的内容，根据内容添加对应参数行
        let tr = "<tr>" + $(this).siblings("table").find("tr").eq(-1).html() + "</tr>";
        $(this).siblings("table").append(tr);
    });
    //删除参数行
    $(".del_head").click(function () {
        let check = $(":checked");  //获取复选框
        let table = $(this).siblings("table");  //获取table标签
        if (table.find("tr").length > 2) {  //判断table标签下的tr长度是否大于2
            // 删除处理
            if (check.length > 0) {   // 判断复选框是否选中
                check.parent().parent().remove()
            } else {
                table.find("tr").eq(-1).remove()
            }
        }
    });
    //选项卡
    $(".car_title li").click(function () {
        $(this).addClass("cra").siblings().removeClass("cra");  //点击元素添加背景属性，同胞去除背景的属性
        // 根据点击元素集的索引，点击元素添加激活属性，同胞去除激活的属性
        $(".content div").eq($(this).index()).addClass("active").siblings().removeClass("active");
    });
})

