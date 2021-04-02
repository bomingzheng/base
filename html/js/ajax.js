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
$.ajax({  // 获取项目，添加项目的列表
	url:'http:..www.baidu.com',
	method: 'POST',
	dataType: 'json',
}).done(function (data){
		let pro = $("#pro");     // 获取需要添加元素的节点
		let res = data.data;    //当获取的数据，该数据是个合集
		for(let i in res) {   //遍历该合集
			let option = '<option value="+res[i].id+">'+ res[i].title+'</option>';  // 把遍历的数据放在下拉框标签里面
			pro.append(option )    // 把获取的数据添加到选择的节点
		}
		// change事件: 检测元素值，是否发生变化
		pro.change(function (){
			//检测元素发生变化，触发函数，向接口列表发送ajax请求
			//pro_id  项目id，先获取项目id
			let pro_id = pro.val()   //项目值赋值给项目id
			$.ajax({
				url: '/interface',
				data:{
					'pro_id':pro_id
				},
				type:'POST',
				dataType:'json'
			}).done(function (data){
				let inter = $('#interface');  	// 获取借口下拉框的标签
				if (data.code === '1'){    		// 如果返回值等于1
					inter.empty()  				// 清空该标签的内容，否则会把当前信息和添加的新信息同时展示
					let res = data.data;   		//获取返回的数据。遍历然后加载到页面
					for(let i=0;i<res.length;i++){ //判断获取的返回数据，循环获取
						let option = '<option value="">'+res[i].name+'</option>'  // 把接口名字显示在下拉框
						inter.append(option)   //把构造数据显示在下拉框标签
					}}})})
	// 熟悉jquery的选择器，去页面获取请求数据
	// 发送ajax请求
	// 把返回数据加载到页面，通过jquery操作页面元素和属性
});




