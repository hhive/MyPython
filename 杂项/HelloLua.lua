------Start----基本语法---------------------------
print("Hello,World!");
print("Hello,xiaolong!");
print("Hello,SeanWu!");
print("Show in sublime!");

print("Hello, Yuyongbing!");

function norm (x,y)
	return (x^2 + y^2)^0.5
end

print("(3^2+4^2)^0.5 is equal to " .. norm(3,4));

function twice (x)
	return 2*x;
end

print("twice of 7 is :", twice(7));

colorArray = {
"red",
"yellow",
"green"
};

print(colorArray[0]);

print("color Array from here:\r\n");
for	i = 1,3 do
	print(colorArray[i]);
end

dataArray = {10,9,12};

print(5+3);
print("90" + 12);
print("90" .. 12);
print("abc",tostring(139));

local k= 1;
while k<9 do
	print(k);
--	if(dataArray[k]) then
--		print(dataArray[k]);
--	end
	k=k+1;
end

------End----基本语法-----------------------------

------Start----循环结构---------------------------
temTable = {1,3,5,7,9,110,119,200,1000};

for i,v in ipairs(temTable) do
	print(i,v)
end

function values(t)
	local i = 0;
	return function () i = i + 1; return t[i];end
end

for element in values(temTable) do
	print(element);
end

for i=1,10 do
	print(i.."out");
	for i=1,3 do
		print(i.."in");
	end
end

------End----循环结构-----------------------------

------Start----Table结构-------------------------
testTable = {
	["hello"] = "directory1",
	["sky"] = "directory2",
	["who"] = "directory3",
	["sea"] = "directory4",
	[30] = 9,
	[31] = 12,
}

print(testTable["hello"].."\r\n");
print(testTable["sky"].."\r\n");
print(testTable["who"].."\r\n");
print(testTable["sea"].."\r\n");
print(testTable[30].."\r\n");
print(testTable[31].."\r\n");

testMultiTable = {
	{30,"A",12},
	{31,"B",13},
	{40,"K",15},
}

local keyIdLetterRelayMap = {
-- KeyID,Letter,Relay
	{"Key_Wave",53,144},
	{"Key_1",30,146},
	{"Key_2",31,149},
	{"Key_3",32,147},
	{"Key_4",33,145},
	{"Key_5",34,160},
	{"Key_6",35,166},
	{"Key_7",36,168},
	{"Key_8",37,161},
	{"Key_9",38,187},
	{"Key_0",39,162},
	{"Key_Minus",45,176},
	{"Key_Equal",46,198},
	{"Key_Del",42,197},
	{"Key_Tab",43,148},
	{"Key_Q",20,159},
	{"Key_W",26,158},
	{"Key_E",8,153},
	{"Key_R",21,151},
	{"Key_T",23,163},
	{"Key_Y",28,164},
	{"Key_U",24,165},
	{"Key_I",12,184},
	{"Key_O",18,177},
	{"Key_P",19,178},
	{"Key_L_Bracket",47,199},
	{"Key_R_Bracket",48,200},
	{"Key_BK_slash",49,192},
	{"Key_Caps",57,150},
	{"Key_A",4,152},
	{"Key_S",22,154},
	{"Key_D",7,155},
	{"Key_F",9,170},
	{"Key_G",10,191},
	{"Key_H",11,190},
	{"Key_J",13,185},
	{"Key_K",14,180},
	{"Key_L",15,181},
	{"Key_Semicolon",51,182},
	{"Key_Quota",52,179},
	{"Key_Return",40,201},
	{"Key_L_Shift",225,156},
	{"Key_Z",29,175},
	{"Key_X",27,172},
	{"Key_C",6,167},
	{"Key_V",25,171},
	{"Key_B",5,183},
	{"Key_N",17,188},
	{"Key_M",16,186},
	{"Key_Comma",54,193},
	{"Key_Point",55,194},
	{"Key_FW_Slash",56,195},
	{"Key_R_Shift",229,196},
	{"Key_Globe",3,157},
	{"Key_L_Ctrl",224,173},
	{"Key_L_Alt",226,174},
	{"Key_L_Command",227,169},
	{"Key_Space",44,189},
	{"Key_R_Command",231,202},
	{"Key_R_ALt",230,203},
	{"Key_L_Arrow",80,204},
	{"Key_U_Arrow",82,205},
	{"Key_D_Arrow",81,207},
	{"Key_R_Arrow",79,206}
}
for i = 1,64 do
	for j = 1,3 do
		print(keyIdLetterRelayMap[i][j]);
	end
	print("\r\n");
end
------End----Table结构-----------------------

------Start----文件读写---------------------------
function ReadFile(file_path)
	local ret = nil;
	local path = file_path;
	local f = io.open(path, "r");
	if f == nil then 
		return nil, "failed to open file at: "..path; 
	else
		ret = f:read("*all");
		f:close();
		return ret;
	end
	
end

function folder_check(par)		--check the folder,whether it is exist or not.
	local folder = par;
	local ret = nil;
	ret = os.execute("cd "..folder);
	if tonumber(ret) > 0 then	--the folder is not exist
		os.execute("mkdir "..folder);			--create the folder
	end
end

testString = ReadFile("/Leo/Debug/Learn_Lua/test.txt");
if testString == nil then
	testString = "This is demo data when the txt file not found!";
end

print(testString);

if	string.find(testString,"test") then
	print("Test found!");
else
	print("Test Not Found");
end
------End----文件读写-----------------------------


------Start----字符串处理及十进制、十六进制数转换---------
sn = "ABCDEF1234567890G";
print("SN TO 0x Data");
print("sn is :"..sn);
array = {};
pstr1 = "";
for i = 1,17 do
	-- print(string.byte(sn,i));
	array[i] = string.byte(sn,i);
	pstr1 = pstr1..array[i].." ";
end
print(pstr1);

print("Data To SN String:");
pstr2 = "";
newArray = {};

for i=1,#array do
	-- print(array[i]);
	newArray[i] = (string.format("%#x ",array[i]));
	pstr2 = pstr2..newArray[i];
end

print(pstr2);

pstr3 = "";
for i=1,#newArray do
	pstr3 = pstr3..string.format("%d",newArray[i]).." ";
end
print(pstr3);

num = string.format("%d",tonumber("7500C201000000",16));
if #num > 10 then
	print(num);
end
print(string.format("%d",tonumber("7500C201000000",16)));

------End----字符串处理及十进制、十六进制数转换---------

------Start----字符串匹配---------------------------
place = string.find("hello,world!,ok","%w+,%w+,%w+");
print(place);

place = string.find("hello,worldoka1231,ok","%w+,%w+,%w+");
print(place);

place = string.find("0.3,45623,998.91","%d+%.*%d*,%d+%.*%d*,%d+%.*%d*");
print(place);

place = string.find("0,45623,998","%d+%.*%d*,%d+%.*%d*,%d+%.*%d*");
print(place);

place = string.find("01.91,45623.01,998.08","%d+%.*%d*,%d+%.*%d*,%d+%.*%d*");
print(place);

function __split(str, reps)
	local r = {};
	if (str == nil) then return nil; end
	string.gsub(str, "[^"..reps.."]+", function(w) table.insert(r, w) end);
	return r;
end

temTable = __split("12,34,56,786,90",",");
for i=1,#temTable do
	print(temTable[i]);
end
------End----字符串匹配---------------------------

------Start----系统库和数学库----------------------
print(os.date("%x"));
print(os.date("%X"));
print(os.date("%c"));

trynum = math.huge;
print(trynum);
trysum = trynum + 90;
print(trysum);
trysum = trynum /190;
print(trysum);
trysum = 100/trynum;
print(trysum);
------End----系统库和数学库------------------------

------Start----调试库(获取当前函数名)---------------
function abc()
	print("abcdefg");
	print(debug.getinfo(1).name);
	ownName = debug.getinfo(1).name;
	return ownName;
end

getName = abc();
print(getName);
------End----调试库(获取当前函数名)-----------------