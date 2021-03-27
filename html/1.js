$(function (){

	//前台账号密码登录发送ajax请求
	$('#登录').click(function (){
		// 获取账号
		let name = $('username').val();
		//获取密码
		let pwd = $('password').val();
		//相关加密处理

		//第一种发送ajax请求
		$.ajax({
			url:'http://www.baidu.com',
			type:'GET',
			data:{
				"username":name,
				"password":pwd
			},
			//cache:false,  是否加载缓存
			dataType:'json',   // 期望后台返回的数据类型
			//后台发送ajax请求不同写head数据
			success:function (data){
				//回调函数，发送成功以后调用该函数,返回数据的code码
				if(data.code ==='1'){
					alert(data.msg);
				}else {
					$(this).next().append('<h3>'+ data.msg +'</h3>') //失败在当前节点下面的div加入提示语
					alert(data.msg);}},
			error:function (){//回调函数，发送失败以后调用该函数,返回数据的code码
					alert('请求失败')
			}
		});

		//第二种发送ajax
			$.ajax({
			url:'http://www.baidu.com',
			method:'POST',
			data:{
				'user':name,
				'pwd': pwd},
			dataType:'json'
			}).done(function (data){ //请求成功调用这个方法触发
				if(data.code ==='1'){
					alert(data.msg);
				}else {
					$(this).next().append('<h3>'+ data.msg +'</h3>') //失败在当前节点下面的div加入提示语
					alert(data.msg);}});
			}).fail(function (){  //请求失败调用这个方法触发
				alert("请求失败")})});

		/* 跨域：请求到了其他域名
		ajax默认拦截发送跨域请求，如必须需要使用 把dataType=jsonp(把该参数赋值jsonp)
		使用该参数他会自动带2个参数发送请求：callback 和 _开头的一个参数；
		需要后台服务器支持ajax跨域才可以，就加个jsonp的值数据会变成jsMIME类型的参数进行解析
		*/
		//进入页面直接发送ajax请求
$.ajax({
	url:'http:..www.baidu.com',
	method: 'POST',
	dataType: 'json',
}).done(function (data){
		let pro = $(".pro");
		let res = data.data;   //当获取的数据有多条需要遍历
		for(let i in res) {
			let option = '<option value="res[i].id+">'+ res[i].title+'</option>'
			pro.append(option )
		}

})




