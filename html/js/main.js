$(function () {
		//弹框
			    $("#add").click(function () {
			        // $(".back").addClass("show")});给该元素addClass添加一个显示属性。

			    	$(".back").show() }); // show()是jquery的封装方法
					//点击+号给它绑定点击事件触发函数，弹窗的id添加显示属性
					//

			    $(".alter_quit").click(function () {
			    	$(".back").hide()   }); //hide()是jquery的封装隐藏方法
			        // $(".back").removeClass("show");  给该元素removeClass移除显示属性。
					//关闭按钮点击事件，触发弹窗的隐藏属性


			    $(".pro_tj").click(function () {
			        $(".back").hide()});
					//removeClass("show");jquery的hide方法;

		//侧边栏
		// 	$(".sidebar_list h3").click(function () {
				// $(this).next().show().parent().siblings().children("ul").hide();
				//当前节点的下面的兄弟节点添加显示属性($(this)=当前节点)并对它父节点的兄弟节点的子节点都添加隐藏属性
			// 	$(this).next().toggle().parent().siblings().children("ul").hide();
			  //  toggle()被选元素进行显示隐藏切换
			// });

		// jquery动画
		    $(".sidebar_list h3").click(function () {
		    	$(this).next().slideToggle().parent().siblings().children("ul").slideUp();
		    	//对被选元素进行滑动隐藏和滑动显示，对它的父节点的兄弟节点的子节点通过调整高度来滑动隐藏

			})});




