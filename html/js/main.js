	$(function () {
		//弹框
			    $("#add").click(function () {
			        $(".back").show() });
					//addClass("show");jquery的show方法

			    $(".alter_quit").click(function () {
			        $(".back").hide()   });
					//removeClass("show");

			    $(".pro_tj").click(function () {
			        $(".back").hide()});
					//removeClass("show");jquery的hide方法;

		//侧边栏(jquery动画)
			$(".sidebar_list h3").click(function () {
			    $(this).next().toggle().parent().siblings().children("ul").hide();
			})
			    //链式调用,点击一个按钮会收起其他列表

		// $(".sidebar_list h3").click(function () {
		// 	    $(this).next().slideToggle("slow",function(){
		// 	    	alert("Animation Done.");}).parent().siblings().children("ul").slideUp();
		// 	});


	})