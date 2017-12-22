from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor


data = """

var nowUrl = "";
var pagePrefix = "/ershoufang"
var init = {
isHighQuality:true,//abtest a or b
putAway : 1,//房屋状态－在售、已下架、已售等
display : 1, //是否是已失效房源
hasClickPlayer:false,//标志是否点过播放视频
hasVideo:true,//标志是否是有视频的房源
accessToken:'',
propertyNo : "5011000013875",  //小区编号
propertyId : "5011000013875",  //小区ID(小区成交图表用的数据)
plateId : "611900123",         //板块ID(小区成交图表用的数据)
plateName : "北蔡",     //板块名称(小区成交图表用的数据)
houseSellId : "4823070",         //房源编号(如sh，虚假举报、短信分享用到)
album_current_Index : 0, //相册当前显示图片的索引号
hasAllowedPhoto : "true", //是否有认证户型图
agentList : [ //经纪人列表

{
userName: "王磊",
userCode: "113454",
hostNumber: "4007675005",
extNumber: "248944",
positionName: "A7-高级经纪人",
daikan: "1",
phone: "4007675005转248944",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/113454_150x200.jpg"

},

{
userName: "毛华东",
userCode: "110223",
hostNumber: "4007675005",
extNumber: "248945",
positionName: "A5-高级经纪人",
daikan: "2",
phone: "4007675005转248945",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/110223_150x200.jpg"

},

{
userName: "罗梦香",
userCode: "220597",
hostNumber: "4007675005",
extNumber: "248976",
positionName: "A3-经纪人",
daikan: "1",
phone: "4007675005转248976",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/220597_150x200.jpg"

},

{
userName: "张超",
userCode: "111138",
hostNumber: "4007675005",
extNumber: "248977",
positionName: "M5-高级店经理",
daikan: "1",
phone: "4007675005转248977",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/111138_150x200.jpg"

},

{
userName: "郭玉江",
userCode: "151540",
hostNumber: "4007675005",
extNumber: "248978",
positionName: "A5-高级经纪人",
daikan: "1",
phone: "4007675005转248978",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/151540_150x200.jpg"

},

{
userName: "沈桃桃",
userCode: "179974",
hostNumber: "4007675005",
extNumber: "248979",
positionName: "A4-高级经纪人",
daikan: "1",
phone: "4007675005转248979",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/179974_150x200.jpg"

},

],
agentListPageNo : 1, //经纪人列表当前页码

kanfangList : [ //看房记录列表

{
userName: "罗梦香",
userCode: "220597",
hostNumber: "4007675016",
extNumber: "20365",
date: "2017-12-18",
times : "1",
phone: "4007675016转20365",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/220597_150x200.jpg",

status : "1",
display : "1",
boothStatus:"1",
userTitle:"A3-经纪人",
nintyDaysLook:"6",
},

{
userName: "王磊",
userCode: "113454",
hostNumber: "4007675016",
extNumber: "47772",
date: "2017-12-10",
times : "1",
phone: "4007675016转47772",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/113454_150x200.jpg",

status : "1",
display : "1",
boothStatus:"1",
userTitle:"A7-高级经纪人",
nintyDaysLook:"2",
},

{
userName: "张奎梅",
userCode: "181842",
hostNumber: "4007675016",
extNumber: "34159",
date: "2017-12-09",
times : "3",
phone: "4007675016转34159",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/181842_150x200.jpg",

status : "1",
display : "1",
boothStatus:"1",
userTitle:"M5-高级店经理",
nintyDaysLook:"3",
},

{
userName: "胡炳勇",
userCode: "110076",
hostNumber: "4007675016",
extNumber: "55664",
date: "2017-12-03",
times : "1",
phone: "4007675016转55664",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/110076_150x200.jpg",

status : "1",
display : "1",
boothStatus:"1",
userTitle:"M5-高级店经理",
nintyDaysLook:"1",
},

{
userName: "席晓波",
userCode: "141677",
hostNumber: "4007675016",
extNumber: "19439",
date: "2017-12-02",
times : "1",
phone: "4007675016转19439",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/141677_150x200.jpg",

status : "1",
display : "1",
boothStatus:"1",
userTitle:"M5-高级店经理",
nintyDaysLook:"1",
},

{
userName: "张超",
userCode: "111138",
hostNumber: "4007675016",
extNumber: "12555",
date: "2017-11-26",
times : "1",
phone: "4007675016转12555",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/111138_150x200.jpg",

status : "1",
display : "1",
boothStatus:"1",
userTitle:"M5-高级店经理",
nintyDaysLook:"1",
},

{
userName: "郭玉江",
userCode: "151540",
hostNumber: "4007675016",
extNumber: "22045",
date: "2017-11-11",
times : "1",
phone: "4007675016转22045",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/151540_150x200.jpg",

status : "1",
display : "1",
boothStatus:"1",
userTitle:"A5-高级经纪人",
nintyDaysLook:"2",
},

{
userName: "王震",
userCode: "238050",
hostNumber: "4007675016",
extNumber: "29302",
date: "2017-11-10",
times : "1",
phone: "4007675016转29302",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/238050_150x200.jpg",

status : "1",
display : "1",
boothStatus:"1",
userTitle:"M3-店经理",
nintyDaysLook:"1",
},

{
userName: "沈桃桃",
userCode: "179974",
hostNumber: "4007675016",
extNumber: "32817",
date: "2017-10-28",
times : "1",
phone: "4007675016转32817",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/179974_150x200.jpg",

status : "1",
display : "1",
boothStatus:"1",
userTitle:"A4-高级经纪人",
nintyDaysLook:"1",
},

{
userName: "毛华东",
userCode: "110223",
hostNumber: "4007675016",
extNumber: "12400",
date: "2017-10-21",
times : "2",
phone: "4007675016转12400",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/110223_150x200.jpg",

status : "1",
display : "1",
boothStatus:"1",
userTitle:"A5-高级经纪人",
nintyDaysLook:"2",
},

{
userName: "张士剑",
userCode: "213772",
hostNumber: "4007675016",
extNumber: "66375",
date: "2017-10-19",
times : "1",
phone: "4007675016转66375",
boothStatus : 1,
status : 1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/213772_150x200.jpg",

status : "1",
display : "1",
boothStatus:"1",
userTitle:"A4-高级经纪人",
nintyDaysLook:"1",
},

{
userName: "吴庚晖",
userCode: "228570",
hostNumber: "4007675016",
extNumber: "22663",
date: "2017-10-13",
times : "1",
phone: "4007675016转22663",
boothStatus : 0,
status : -1,


photoUrl: "http://cdn1.dooioo.com/fetch/vp/touxiang/photos/228570_150x200.jpg",

status : "-1",
display : "0",
boothStatus:"0",
userTitle:"A2-经纪人",
nintyDaysLook:"1",
},

],
kanfangListPageNo : 1, //看房记录列表当前页码

recommendList : [ //推荐房源列表

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20161121/290c7b5a-acd9-4324-82eb-520dcbfc997e.jpg_200x150.jpg",

price: "460",
name: "海东公寓",
room: "2",
hall: "2",
area: "83.44",
cityCode:"sh",
houseSellId: "4378650"
},

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20160828/6783252b-4b7c-4360-ba68-aa70180738df.jpg_200x150.jpg",

price: "455",
name: "海东公寓",
room: "2",
hall: "2",
area: "87.6",
cityCode:"sh",
houseSellId: "4590814"
},

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20170520/cd9a663d-7210-47d0-ac81-a4b8bb6caeac.jpg_200x150.jpg",

price: "470",
name: "海东公寓",
room: "2",
hall: "2",
area: "87.25",
cityCode:"sh",
houseSellId: "4631998"
},

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20151117/eff63c78-7133-4841-a8d0-a3043100dfa8.jpg_200x150.jpg",

price: "498",
name: "海东公寓",
room: "2",
hall: "2",
area: "88.38",
cityCode:"sh",
houseSellId: "4817692"
},

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20160810/0ad12b20-0807-459b-acfe-507eadd49a96.jpg_200x150.jpg",

price: "460",
name: "海东公寓",
room: "2",
hall: "2",
area: "79.13",
cityCode:"sh",
houseSellId: "4195917"
},

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20170730/cf8c52e5-92da-4693-b702-7ff58125a769.jpg_200x150.jpg",

price: "465",
name: "海东公寓",
room: "2",
hall: "2",
area: "79.22",
cityCode:"sh",
houseSellId: "4737078"
},

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20161024/7e86d110-8fc8-4064-8554-f21a2a07d086.jpg_200x150.jpg",

price: "490",
name: "海东公寓",
room: "2",
hall: "2",
area: "79.22",
cityCode:"sh",
houseSellId: "4352456"
},

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20170917/2e12f79c-99ed-41e6-8496-4399d1dfa699.jpg_200x150.jpg",

price: "500",
name: "海东公寓",
room: "2",
hall: "2",
area: "82.79",
cityCode:"sh",
houseSellId: "4797252"
},

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20170617/a5d61121-a382-4fde-b676-1a801a323952.jpg_200x150.jpg",

price: "430",
name: "芳华路253弄",
room: "2",
hall: "2",
area: "72.65",
cityCode:"sh",
houseSellId: "4685621"
},

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20161217/ee59609e-dc83-4bd7-93c4-0473380aca0a.jpg_200x150.jpg",

price: "445",
name: "南杨花园",
room: "2",
hall: "2",
area: "78.78",
cityCode:"sh",
houseSellId: "4356875"
},

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20170401/10071442-3d7d-48f8-911b-f5a07c9abe3b.jpg_200x150.jpg",

price: "390",
name: "莲鼎苑",
room: "2",
hall: "1",
area: "69.2",
cityCode:"sh",
houseSellId: "4805154"
},

{


photourl: "http://cdn1.dooioo.com/fetch/vp/fy/gi/20170112/b4897db0-363e-4351-a1d2-391d60a5fac8.jpg_200x150.jpg",

price: "435",
name: "聚龙家园",
room: "2",
hall: "1",
area: "74.07",
cityCode:"sh",
houseSellId: "4483519"
},

],
recommendListPageNo : 1, //看房记录列表当前页码
vid:"6e5dded0425f44a594f5e4de754baa61",

gio : {//GrowingIO页面相关业务参数收集的数据初始化
"setPageGroup" : "二手房", //页面名称
"setPS1" : "sh4823070", //房源编号
"setPS2" : "2", //户型图类型ID
"setPS3" : "1", //有无视频 0-无视频，1-有视频
},
firstPayInfo:[


{
"total":"210.63",
"totalUnit":"万",

"firstMinPay":"164.5",
"firstMinPayUnit":"万",

"referenceTax":"36.73",
"referenceTaxUnit":"万",

"addedTax":"23.25",
"addedTaxUnit":"万",

"personalIncomeTax":"8.98",
"personalIncomeTaxUnit":"万",

"deedTax":"4.49",
"deedTaxUnit":"万",

"intermediaryServiceCharge":"9.4",
"intermediaryServiceChargeUnit":"万"
},

{
"total":"384.12",
"totalUnit":"万",

"firstMinPay":"329.0",
"firstMinPayUnit":"万",

"referenceTax":"45.72",
"referenceTaxUnit":"万",

"addedTax":"23.25",
"addedTaxUnit":"万",

"personalIncomeTax":"8.98",
"personalIncomeTaxUnit":"万",

"deedTax":"13.48",
"deedTaxUnit":"万",

"intermediaryServiceCharge":"9.4",
"intermediaryServiceChargeUnit":"万"
},


]
}


//晶赞统计, 老客回访代码
window.__zp_tag_params = {
p_zp_prodstype: "e956f65aa6d09b919e340dc0b9fb119b",
category: headerParameters.cityName,
productID: 'sh4823070',
p_zp_prods:{
"outerid": 'sh4823070',
"loc": location.href,
"name": '海东公寓',
"image": 'http://cdn1.dooioo.com/fetch/vp/fy/gi/20171013/f895c4e1-6c56-43a6-8147-37f21e6046a5.jpg_200x150.jpg',
"totalprice": '470',
"unitprice": '56327',
"housetype": '2室2厅',
"area": '83.44',
"category": headerParameters.cityName,
"subcategory": '浦东',
"thirdcategory": '北蔡',
"monthlypayment": '16214',
"level": '高区/6层',
"facing": '南',
"community": '海东公寓（浦东 北蔡）',
"downpayment": '164.5',
"decoration": '简装',
"buildingage": '1997年建',
"address": '莲园路100弄',
"subway": '距离7号线锦绣路站788米'
}
};
function initSaveSearch() {}

"""

parser = Parser()
tree = parser.parse(data)
fields = {
	getattr(node.left, 'value', ''): getattr(node.right, 'value', '')
	for node in nodevisitor.visit(tree)
		if isinstance(node, ast.Assign)
	}

print(fields['date'])
