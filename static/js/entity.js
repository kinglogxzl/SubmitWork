


 $(".f_upload").fileinput({
     theme: 'zh',
     language: 'zh',
     showUpload: false,
     previewSettings: {
         image: {width: "500px", height: "500px"}
     },
     msgPlaceholder: "选择输入文件",
     uploadUrl: "/entity/train_model", //上传的地址
 })
