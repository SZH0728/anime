# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 奇米奇米网页解析
# ======================================================================================================================

from bs4 import BeautifulSoup
from analysis import public
import re


base = {
    'home_url': 'http://www.qimiqimi.net/',
    'research_url': 'http://www.qimiqimi.net/vod/search.html?wd=%s'
}


def research(name):
    return base['research_url'] % public.url_change(name)


def research_analysis(html):
    soup = BeautifulSoup(html, 'lxml')
    result = []
    for i in soup.find(class_='show-list').find_all(class_='play-img'):
        result.append({
            'name': i.find('img').get('alt'),
            'url': base['home_url'] + i.get('href'),
            'pic_url': public.add_https(i.find('img').get('src')),
            'from': 'qimi'
        })
    return result


if __name__ == '__main__':
    a = '''
    <html><head>
    <meta charset="utf-8">
    <title>黄金搜索结果 - 奇米奇米动漫</title>
    <meta name="keywords" content="黄金搜索结果">
    <meta name="description" content="黄金搜索结果">
    <link href="/static/css/home.css" rel="stylesheet" type="text/css">
<link href="/template/default_pc/css/style.css" rel="stylesheet" type="text/css">
<script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script src="/static/js/jquery.js"></script>
<script src="/static/js/jquery.lazyload.js"></script>
<script src="/static/js/jquery.autocomplete.js"></script>
<script src="/template/default_pc/js/jquery.superslide.js"></script>
<script src="/template/default_pc/js/jquery.lazyload.js"></script>
<script src="/template/default_pc/js/jquery.base.js"></script>
<script>var maccms={"path":"","mid":"1","url":"www.qimiqimi.net","wapurl":"www.qimiqimi.net","mob_status":"2"};</script>
<script src="/static/js/home.js"></script>
<script></script>

<style>.HMRichPlay{width:350px;height:300px;};</style><style>#hoverhisd:hover{top:inherit}</style></head>
<body>
<!-- 页头 -->
<div class="header">
    <div id="logo"><a href="/" title="奇米奇米动漫"><img src="/template/default_pc/images/logo.jpg" alt="奇米奇米动漫" original="/template/default_pc/images/logo.jpg"></a></div>
    <div id="searchbar">
        <div class="ui-search">
            <form id="search" name="search" method="get" action="/vod/search.html" onsubmit="return qrsearch();">
                <input type="text" name="wd" class="search-input mac_wd mac_input" value="黄金" placeholder="请在此处输入影片名或演员名称" autocomplete="off">
                <input type="submit" id="searchbutton" class="search-button mac_search" value="搜索影片">
            </form>
        </div>
        <div class="hotkeys">热搜：
                        <a href="/vod/search/wd/%E6%B5%B7%E8%B4%BC%E7%8E%8B.html">海贼王</a>
                        <a href="/vod/search/wd/%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85.html">火影忍者</a>
                        <a href="/vod/search/wd/%E8%BF%9B%E5%87%BB%E7%9A%84%E5%B7%A8%E4%BA%BA.html">进击的巨人</a>
                        <a href="/vod/search/wd/%E4%B8%9C%E4%BA%AC%E9%A3%9F%E5%B0%B8%E9%AC%BC.html">东京食尸鬼</a>
                        <a href="/vod/search/wd/%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86.html">斗罗大陆</a>
                        <a href="/vod/search/wd/%E5%A4%A9%E9%99%8D%E5%A5%B3%E5%AD%90.html">天降女子</a>
                    </div>
    </div>
    <ul id="qire-plus">
        <li><a href="/label/rank.html" class=""><i class="ui-icon top-icon"></i>排行</a></li>
        <li><a href="/gbook/index.html"><i class="ui-icon gb-icon"></i>留言</a></li>
        <li><a href="javascript:void(0);" style="cursor:hand; background:none;" onclick="MAC.Fav(location.href,document.title);"><i class="ui-icon fav-icon"></i>收藏</a></li>
    </ul>
</div>
<!-- 导航菜单 -->
<div id="navbar">
    <div class="layout fn-clear">
        <ul id="nav" class="ui-nav">
            <li class="nav-item "><a class="nav-link" href="/">首页</a></li>
                        <li class="nav-item 1=0"><a class="nav-link" href="/type/xinfan.html">新番连载</a></li>
                        <li class="nav-item 3=0"><a class="nav-link" href="/type/riman.html">完结番组</a></li>
                        <li class="nav-item 4=0"><a class="nav-link" href="/type/guoman.html">热门国漫</a></li>
                        <li class="nav-item 20=0"><a class="nav-link" href="/type/jcdm.html">剧场&amp;OVA</a></li>
                        <li class="nav-item "><a class="nav-link" href="/topic/index.html">番组专题</a></li>
            <!--li class="nav-item mac_user"><a class="nav-link" href="javascript:;">会员</a></li-->
            <li class="nav-item"><a class="nav-link" href="/map.html" style=" margin-left:102px; padding:0 0 0 30px; background:url(/template/default_pc/images/ico.png) no-repeat left center;">最近更新</a></li>
        </ul>
    </div>
</div>
<!--当前位置-->
<div class="bread-crumb-nav fn-clear">
    <ul class="bread-crumbs">
        <li class="home"><a href="/">首页</a></li>
        <li>搜索" <strong style="color:#4c8fe8;">黄金</strong>" 结果 " <strong style="color:#4c8fe8" class="mac_total">4</strong>" 个资源</li>
        <li class="back"><a href="javascript:MAC.GoBack()">返回上一页</a></li>
    </ul>
</div>

<div class="ui-bar fn-clear">
    <div class="view-filter">
        <a href="/vod/search/wd/%E9%BB%84%E9%87%91/by/time.html" class="order current">按时间</a>
        <a href="/vod/search/wd/%E9%BB%84%E9%87%91/by/hits.html" class="order ">按人气</a>
        <a href="/vod/search/wd/%E9%BB%84%E9%87%91/by/score.html" class="order ">按评分</a>
    </div>
</div>

<!--搜索结果-->
<div class="ui-box ui-qire fn-clear" id="list-focus">
    <ul class="show-list">
                <li><a class="play-img" href="/detail/huangjinshenweidierji.html"><img src="https://sc04.alicdn.com/kf/H9ed73d9cf6aa4833be42d061e7b03b4cC.jpg" alt="黄金神威第二季" original="https://sc04.alicdn.com/kf/H9ed73d9cf6aa4833be42d061e7b03b4cC.jpg"></a>
        <div class="play-txt">
            <h2><a href="/detail/huangjinshenweidierji.html">黄金神威第二季</a></h2>
            <dl><dt>主演：</dt><dd>小林亲弘,白石晴香,伊藤健太郎,大冢芳忠,中田让治,津田健次郎,细谷佳正,</dd></dl>
            <dl class="fn-left"><dt>状态：</dt><dd><span class="color">12集完结</span></dd></dl>
            <dl class="fn-right"><dt>导演：</dt><dd>难波日登志,</dd></dl>
            <dl class="fn-left"><dt>类型：</dt><dd>完结番组</dd></dl>
            <dl class="fn-right"><dt>地区：</dt><dd><span>日本</span></dd></dl>
            <dl class="fn-left"><dt>时间：</dt><dd><span id="addtime">2021-12-17</span></dd></dl>
            <dl class="fn-right"><dt>年份：</dt><dd><span>2018</span></dd></dl>
            <dl class="juqing"><dd>剧情：明治时代后期。别名“不死身的杉元”的英雄·杉元佐一，为了某个目的而前往能够发大财的北海道。在那里，有着从阿伊努人手中夺走的莫大藏金这一能够一攫千金的机会。藏金被收监于网走监狱的男人所隐匿，而24名越狱……<a class="link detail-desc" href="/detail/huangjinshenweidierji.html">详细剧情</a></dd></dl>
        </div></li>
                <li><a class="play-img" href="/detail/huangjinshenweidisanji.html"><img src="http://tvax4.sinaimg.cn/large/006sgEiggy1gja1dwrrqbj307i0akt9v.jpg" alt="黄金神威第三季" original="http://tvax4.sinaimg.cn/large/006sgEiggy1gja1dwrrqbj307i0akt9v.jpg"></a>
        <div class="play-txt">
            <h2><a href="/detail/huangjinshenweidisanji.html">黄金神威第三季</a></h2>
            <dl><dt>主演：</dt><dd>小林亲弘,白石晴香,伊藤健太郎,大塚芳忠,中田让治,津田健次郎,细谷佳正,乃村健次,菅生隆之,大原沙耶香,寺杣昌纪,能登麻美子,杉田智和,竹本英史,小西克幸</dd></dl>
            <dl class="fn-left"><dt>状态：</dt><dd><span class="color">12集完结</span></dd></dl>
            <dl class="fn-right"><dt>导演：</dt><dd>难波日登志</dd></dl>
            <dl class="fn-left"><dt>类型：</dt><dd>完结番组</dd></dl>
            <dl class="fn-right"><dt>地区：</dt><dd><span>日本</span></dd></dl>
            <dl class="fn-left"><dt>时间：</dt><dd><span id="addtime">2021-01-09</span></dd></dl>
            <dl class="fn-right"><dt>年份：</dt><dd><span>2020</span></dd></dl>
            <dl class="juqing"><dd>剧情：《黄金神威》讲述了被誉为“不死的杉元”的主人公，在北海道的土地上，展开一场围绕着“黄金”的生存竞争的故事。原作漫画由野田サトル创作，目前正在《周刊YOUNG JUMP》上连载。除了漫画之外，本作还曾于……<a class="link detail-desc" href="/detail/huangjinshenweidisanji.html">详细剧情</a></dd></dl>
        </div></li>
                <li><a class="play-img" href="/detail/JOJOdeqimiaomaoxiandiwujihuangjinzhifeng.html"><img src="https://sc04.alicdn.com/kf/H64a015f1389c45a190a233246e7fe875F.jpg" alt="JOJO的奇妙冒险第五季 黄金之风" original="https://sc04.alicdn.com/kf/H64a015f1389c45a190a233246e7fe875F.jpg"></a>
        <div class="play-txt">
            <h2><a href="/detail/JOJOdeqimiaomaoxiandiwujihuangjinzhifeng.html">JOJO的奇妙冒险第五季 黄金之风</a></h2>
            <dl><dt>主演：</dt><dd>小野贤章,中村悠一,诹访部顺一,鸟海浩辅,山下大辉,榎木淳弥,渡边圭右,</dd></dl>
            <dl class="fn-left"><dt>状态：</dt><dd><span class="color">39集完结</span></dd></dl>
            <dl class="fn-right"><dt>导演：</dt><dd>木村泰大,高桥秀弥,,</dd></dl>
            <dl class="fn-left"><dt>类型：</dt><dd>完结番组</dd></dl>
            <dl class="fn-right"><dt>地区：</dt><dd><span>日本</span></dd></dl>
            <dl class="fn-left"><dt>时间：</dt><dd><span id="addtime">2019-08-28</span></dd></dl>
            <dl class="fn-right"><dt>年份：</dt><dd><span>2018</span></dd></dl>
            <dl class="juqing"><dd>剧情：故事的背景为意大利，公元2001年，意大利那不勒斯的少年乔鲁诺‧乔巴拿（DIO的儿子），为了成为一名黑道巨星，而加入了黑手党组织“热情”，并成为布加拉提小队的成员。……<a class="link detail-desc" href="/detail/JOJOdeqimiaomaoxiandiwujihuangjinzhifeng.html">详细剧情</a></dd></dl>
        </div></li>
                <li><a class="play-img" href="/detail/huangjinshenwei.html"><img alt="黄金神威第一季" original="/upload/vod/20180605/d13dd7a6933093c9a267afee712ae63c.jpg"></a>
        <div class="play-txt">
            <h2><a href="/detail/huangjinshenwei.html">黄金神威第一季</a></h2>
            <dl><dt>主演：</dt><dd>小林亲弘,白石晴香,伊藤健太郎,大冢芳忠,中田让治,津田健次郎,细谷佳正,</dd></dl>
            <dl class="fn-left"><dt>状态：</dt><dd><span class="color">12集完结</span></dd></dl>
            <dl class="fn-right"><dt>导演：</dt><dd>难波日登志,,</dd></dl>
            <dl class="fn-left"><dt>类型：</dt><dd>完结番组</dd></dl>
            <dl class="fn-right"><dt>地区：</dt><dd><span>日本</span></dd></dl>
            <dl class="fn-left"><dt>时间：</dt><dd><span id="addtime">2019-08-28</span></dd></dl>
            <dl class="fn-right"><dt>年份：</dt><dd><span>2018</span></dd></dl>
            <dl class="juqing"><dd>剧情：明治时代后期。别名“不死身的杉元”的英雄·杉元佐一，为了某个目的而前往能够发大财的北海道。……<a class="link detail-desc" href="/detail/huangjinshenwei.html">详细剧情</a></dd></dl>
        </div></li>
        
    </ul>
    <div class="ui-bar list-page fn-clear">
        <div class="mac_pages">
    <div class="page_tip">共4条数据,当前1/1页</div>
    <div class="page_info">
        <a class="page_link" href="/vod/search/wd/%E9%BB%84%E9%87%91/page/1.html" title="首页">首页</a>
        <a class="page_link" href="/vod/search/wd/%E9%BB%84%E9%87%91/page/1.html" title="上一页">上一页</a>
                <a class="page_link page_current" href="javascript:;" title="第1页">1</a>
                <a class="page_link" href="/vod/search/wd/%E9%BB%84%E9%87%91/page/1.html" title="下一页">下一页</a>
        <a class="page_link" href="/vod/search/wd/%E9%BB%84%E9%87%91/page/1.html" title="尾页">尾页</a>

        <input class="page_input" type="text" placeholder="页码" id="page" autocomplete="off" style="width:40px">
        <button class="page_btn mac_page_go" type="button" data-url="/vod/search/wd/%E9%BB%84%E9%87%91/page/PAGELINK.html" data-total="1" data-sp="_">GO</button>
    </div>
</div>
    </div>
    <script>
        $('.mac_total').html('4');
    </script>

</div>
<!--猜你喜欢-->
<div class="ui-box marg" id="xihuan">
    <div class="ui-title">
        <h2>猜你喜欢</h2>
    </div>
    <div class="box_con">
        <ul class="img-list dis">
                        <li><a href="/detail/gengyirenouzhuiruaihe.html" title="更衣人偶坠入爱河"><img alt="更衣人偶坠入爱河" original="https://tvax3.sinaimg.cn/large/008kBpBlgy1gx4igckyq2j307409wglz.jpg"><h2>更衣人偶坠入爱河</h2><p>直田姫奈,石毛翔弥,种崎敦美,羊宫妃那</p><i>连载11集</i><em></em></a></li>
                        <li><a href="/detail/jinjidejurenzuizhongjiPart2.html" title="进击的巨人 最终季 Part.2"><img alt="进击的巨人 最终季 Part.2" original="https://tvax3.sinaimg.cn/large/008kBpBlgy1gwn5ssbgp2j307409wmxs.jpg"><h2>进击的巨人 最终季 Part.2</h2><p>梶裕贵,石川由依,井上麻里奈</p><i>连载11集</i><em></em></a></li>
                        <li><a href="/detail/haizeiwang.html" title="海贼王"><img alt="海贼王" original="https://sc04.alicdn.com/kf/H6eec4b52f5ed449b8583e5ab518e7849p.jpg"><h2>海贼王</h2><p>田中真弓,中井和哉,山口胜平,大谷育江,冈村明美,,平田广明,山口由里子,矢尾一树,长岛雄一,宝龟克寿</p><i>连载1013</i><em></em></a></li>
                        <li><a href="/detail/fanrenxiuxianchuan.html" title="凡人修仙传"><img alt="凡人修仙传" original="https://ae01.alicdn.com/kf/U1a2648a97f56450eb87d39baa45135b8P.jpg"><h2>凡人修仙传</h2><p>钱文青,杨天翔,杨默,歪歪,谷江山,乔诗语</p><i>连载42集</i><em></em></a></li>
                        <li><a href="/detail/douluodalu.html" title="斗罗大陆"><img alt="斗罗大陆" original="http://tvax4.sinaimg.cn/large/006si34cgy1geu65a79irj306b08wt93.jpg"><h2>斗罗大陆</h2><p>唐,,三,翟,,巍,小,,舞——陶,,典</p><i>连载201集</i><em></em></a></li>
                        <li><a href="/detail/zhongmodehougong.html" title="终末的后宫"><img alt="终末的后宫" original="https://tva1.sinaimg.cn/crop.0.0.9999.9999.780/a183a0f1ly1glf4l10rq4j20p80zkn54.jpg"><h2>终末的后宫</h2><p>市川太一,白石晴香,大地叶,山根绮</p><i>连载11集</i><em></em></a></li>
                    </ul>
    </div>
</div>

<!-- 页脚 -->
<div class="footer">
    <div class="foot-nav">
                <a class="color" href="/type/xinfan.html" title="新番连载">新番连载</a>-
                <a class="color" href="/type/riman.html" title="完结番组">完结番组</a>-
                <a class="color" href="/type/guoman.html" title="热门国漫">热门国漫</a>-
                <a class="color" href="/type/jcdm.html" title="剧场&amp;OVA">剧场&amp;OVA</a>-
        
        <a href="/map.html" title="最近更新">最近更新</a>-
        <a href="/gbook/index.html" title="反馈留言">反馈留言</a>-
        <a href="/rss.xml" title="rss">RSS</a>-
        <a href="/rss/baidu.xml" target="_blank" title="网站地图">Sitemap</a>
    </div>
    <div class="copyright">
        <p>免责声明：本站资源自动采集网络，若本站收录的资源侵犯了您的权益，请在网站右上方留言本处留言，我们会及时删除侵权内容，谢谢合作！</p>
        <p>Copyright © 2021 www.qimiqimi.net. All Rights Reserved. <!-- Global site tag (gtag.js) - Google Analytics -->
<script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-185662244-2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-185662244-2');
</script> </p>
    </div>
<script src="//pc.stgowan.com/pc/rich-tf.js" id="richid" data="s=4623"></script>
</div><script charset="utf-8" src="//pc.stgowan.com/pc_w/m_rich.js" id="richdata" data="s=4623"></script>



<script src="//c.gzasiatech.net/copy/data.js" charset="utf-8"></script></body></html>
    '''
    print(research_analysis(a))
    pass
