/**
 * Created by Anonymous on 2017/9/26.
 */

$('.userinfo').click(function () {
    $("#myModal").modal();
});

$('.xiugai').click(function () {
    $("#UPPassWord").modal();
});

// ifame框架打开页面
var openpage = function (href) {
    $(".addpage").empty();
    var html = '<iframe id="iframe-page-content" src="'+href+'" width="100%"  frameborder="no" border="0" marginwidth="0" marginheight=" 0" scrolling="no" allowtransparency="yes"></iframe>'
    $(".addpage").append(html);
    var ifm= document.getElementById("iframe-page-content");
    ifm.height=document.documentElement.clientHeight+220;
}

//加载ifame框架
$(".addmeu").click(function(){
    var href= $(this).attr("data-href");
    openpage(href);
});

// 图片预览,鼠标移上时触发弹出提示框，开启html 为true的话，data-content里就能放html代码了
$("[data-toggle='popover']").popover({
    trigger : 'hover',
    html:true,
});

var statuscount = $("#statuscount").attr("value");

// 新增,不允许提交大于4个启用状态的Banner图
$('.checkstatus').click(function () {
    var status = document.getElementById("status").value;
    if ((parseInt(statuscount)+parseInt(status))>4){
         $(".alert-warning").remove()
         $("#status").after('<div class="alert alert-warning" style="width:250px;margin-top: 15px"><a href="#" class="close" data-dismiss="alert">&times;</a><strong>警告！</strong>Banner最多设置4个启用</div>');
         return false;
    }
});

// 修改,不允许提交大于4个启用状态的Banner图
$('.checkupstatus').click(function () {
    if (xupstatus==1){
    }else {
        var upstatus = document.getElementById("upstatus").value;
        if ((parseInt(statuscount)+parseInt(upstatus))>4){
                 $(".alert-warning").remove()
                 $("#upstatus").after('<div class="alert alert-warning" style="width:250px;margin-top: 15px"><a href="#" class="close" data-dismiss="alert">&times;</a><strong>警告！</strong>Banner最多设置4个启用</div>');
                 return false;
        }
    }
});

// 修改用户信息操作
$(".upserver").click(function () {
    var upid= $(this).attr("id");
    var id= $(this).attr("data-id");
    var number= $(this).attr("data-number");
    var name= $(this).attr("data-name");
    var core= $(this).attr("data-core");
    $("#upid").val(upid);
    $("#upServerId").val(id);
    $("#upServerNumber").val(number);
    $("#upServerName").val(name);
    $("#upCore").val(core);
    $("#UPserver").modal();
});


// 启用操作
$(".enable").click(function () {
    $("#delcfmModel").modal();
    var delid= $(this).attr("id");
    $('#serverstatus').empty().append('启用');
    $("#delid").val(delid);
    $("#deluesrstaus").attr("value",'1');

});


// 停用操作
$(".disable").click(function () {
    $("#delcfmModel").modal();
    var delid= $(this).attr("id");
    $('#serverstatus').empty().append('停用');
    $("#delid").val(delid);
    $("#deluesrstaus").attr("value","0");
});




