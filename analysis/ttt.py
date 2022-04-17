# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 233动漫网页解析
# ======================================================================================================================

from bs4 import BeautifulSoup
from analysis import other
from broswer import add
import re

base = {
    'home_url': 'https://www.dm233.cc',
    'research_url': 'https://www.dm233.cc/search?keyword=%s&seaex=1'
}


def research(name):
    return add(
        url=base['research_url'] % other.url_change(name),
        xpath='/html/body/div[2]/div/div/div[1]/section/div[3]',
        other=['ttt', 'research']
    )


def detail(url):
    return add(
        url=url,
        xpath='/html/body/div[2]/div/div/div[3]/section[2]/div/div',
        other=['ttt', 'detail'],
        timeout=15
    )


def research_analysis(html):
    soup = BeautifulSoup(html, 'lxml')
    result = []
    for i in soup.find(class_='dhnew adj1').find_all('li'):
        result.append({
            'name': i.find('a').get('title'),
            'url': base['home_url'] + i.find('a').get('href'),
            'pic': other.pic_show(other.add_https(i.find('img').get('src'))),
            'from': 'ttt'
        })
    return result


def detail_analysis(html):
    soup = BeautifulSoup(html, 'lxml')
    play = []
    info = soup.find(class_='info')
    sinfo = soup.find(class_='normal-nei1 dhxx anime_info').find_all('p')
    for index, i in enumerate(soup.find(class_='normal-nei3').find_all(class_='eplist-eppic')):
        play.append([])
        for p in i.find_all('li'):
            play[index].append({
                'name': other.video_name_change(p.find('p').string),
                'url': base['home_url'] + p.find('a').get('href')
            })
    # b = str(info.find(id='box', class_='info2').find('p'))
    # b = b.replace('<p>', '')
    # b = b.replace('<strong>简介：</strong>', '')
    # b = b.replace('</p>', '')
    # b = b.strip()
    return {
        'name': other.name_change(info.find(class_='h1-title').string),
        'from': 'ttt',
        'auther': sinfo[6].string.split('：')[1],
        'pic': other.pic_show(other.add_https(soup.find(class_="anime-img").find('img').get('src'))),
        'time': re.findall(r'(\d*-\d*-\d*)', sinfo[-3].string)[0],
        'model': sinfo[9].string.split('：')[1],
        'info': '没有数据',
        'play': play
    }


def video_analysis(iframe):
    soup = BeautifulSoup(iframe, 'lxml')
    try:
        soup.find('video').get('src')
    except AttributeError:
        return None


if __name__ == '__main__':
    a = '''
<!DOCTYPE html>
<html lang="zh">
  
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>黄金神威 第三季 - 在线观看-全集动漫下载-233动漫</title>
    <meta name="keywords" content="黄金神威 第三季" />
    <meta name="description" content="电视动画「黄金神威」第3季第2弹PV公开，片头曲 「Grey」与片尾曲「融雪」分别由 FOMARE 和 THE SIXTH LIE 演唱。该作将从10月5日起播出。杉元佐一为了得到大量的黄金，来到了昔日淘金热潮盛行的北海道。机缘巧合下他得知了隐藏著阿依努人庞大财宝的线索......在充满威严的大自然..." />
    <meta name="renderer" content="webkit">
    <meta name="full-screen" content="yes" />
    <meta name="x5-fullscreen" content="true">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <meta name="applicable-device" content="pc,mobile">
    <link rel="shortcut icon" href="/yxsf/pic/favicon.ico" type="image/vnd.microsoft.icon">
    <link href="/yxsf/css/yx_base.css?ver=202008090445" rel="stylesheet" type="text/css">

    <link href="/yxsf/css/yx_art.css?ver=202011300081" rel="stylesheet" type="text/css">
    <link href="/yxsf/css/comment.zero.css?ver=202011300081" rel="stylesheet" type="text/css">

    <script type="text/javascript" src="/yxsf/js/headimgs.js?ver=202011300081"></script>
    <script type="text/javascript" src="/yxsf/jquery/1.12.4/jquery.min.js?ver=202011300081"></script>
    <script type="text/javascript" src="/yxsf/js/yx_jquery.cookie.js"></script>
    <script type="text/javascript" src="/yxsf/js/yx_base64.js"></script>
    <script type="text/javascript" src="/yxsf/js/yx_playpre10.js?ver=202011300081"></script>
    

    <!---->
    <script>var isfof = '';
      var jsUrl = $.cookie('user_script_url');
    </script>
    <base target="_self" />
  </head>
  
  <body>

    


<div class="aclogin">
    <div class="ct">
      <div class='updatenum'>近三天更新动画
        <strong>
          <a title="近三天更新动画" href="/catalog/" target="_self">233</a></strong>部</div>
      <div class="bdsharebuttonbox bdadj">
        <a href="#" class="bds_fbook" data-cmd="fbook" title="分享到Facebook"></a>
        <a href="#" class="bds_twi" data-cmd="twi" title="分享到Twitter"></a>
        <a href="#" class="bds_tieba" data-cmd="tieba" title="分享到百度贴吧"></a>
        <a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a>
        <a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博"></a>
        <a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a>
        <a href="#" class="bds_more" data-cmd="more"></a>
      </div>
      <script>window._bd_share_config = {
          "common": {
            "bdSnsKey": {},
            "bdText": "",
            "bdMini": "2",
            "bdMiniList": false,
            "bdPic": "",
            "bdStyle": "0",
            "bdSize": "16"
          },
          "share": {}
        };
        with(document) 0[(getElementsByTagName('head')[0] || body).appendChild(createElement('script')).src = '/yxsf/static/api/js/share.js?ver=202011300081'];</script>
      <div class="settings">
        <a href="/" target="_self">首页</a></div>
      <div class='locale'>
        <script type="text/javascript" src="/yxsf/js/yx_locale.js?20190218"></script>
      </div>
    </div>
  </div>




    <div id="page-back" class="page-back">

      <!--bgshow-->
      <script type="text/javascript" src="/yxsf/js/yx_bgshow.js"></script>

      <div class="page">

        


<header class="header" role="banner">
    <div class="logo">
      <a title="动漫下载" href="/" target="_self">233动漫</a></div>
    <div class="nav clearfix" id="nav" role="navigation">
      <div class="nav1">
        <nav class="nav-main">
          <ul>

            
    <li>
        <a title="动漫下载首页" href="/" target="_self">首页</a></li>
    <li>
        <a title="动漫目录" href="/catalog/" target="_self">目录</a></li>
    <li>
        <a title="2022年1月新番" href="/catalog/?year=2022&season=1&region=%E6%97%A5%E6%9C%AC" target="_self">2022年1月新番</a></li>
    <li>
        <a title="2021年10月新番" href="/catalog/?year=2021&season=10&region=%E6%97%A5%E6%9C%AC" target="_self">2021年10月新番</a></li>
    <li>
        <a title="完结动漫下载" href="/catalog/?status=%e5%ae%8c%e7%bb%93" target="_self">完结动画</a></li>
    <li>
        <a title="每日动漫推荐" href="/recommend/" target="_self">每日推荐<span class="find-light-icon"></span></a></li>
    <li>
        <a title="动漫资讯" href="/article/" target="_self">动漫资讯</a></li>
    <li>
        <a title="动画排行" href="/rank/" target="_self">排行榜</a></li>
    <li>
        <a title="公告栏" href="/upreports/" target="_self">公告栏</a></li>
    
            
          </ul>
        </nav>
      </div>
      <div class="nav2">
        <nav class="nav-search">
          <ul>

            <li><a title="海贼王" href="/family/%e6%b5%b7%e8%b4%bc%e7%8e%8b.html">海贼王</a></li>

            <li><a title="银魂" href="/family/%e9%93%b6%e9%ad%82.html">银魂</a></li>

            <li><a title="一拳超人" href="/family/%e4%b8%80%e6%8b%b3%e8%b6%85%e4%ba%ba.html">一拳超人</a></li>

            <li><a title="食戟之灵" href="/family/%e9%a3%9f%e6%88%9f%e4%b9%8b%e7%81%b5.html">食戟之灵</a></li>

            <li><a title="刀剑神域" href="/family/%e5%88%80%e5%89%91%e7%a5%9e%e5%9f%9f.html">刀剑神域</a></li>

            <li><a title="进击的巨人" href="/family/%e8%bf%9b%e5%87%bb%e7%9a%84%e5%b7%a8%e4%ba%ba.html">进击的巨人</a></li>

            <li><a title="JOJO的奇妙冒险" href="/family/JOJO%e7%9a%84%e5%a5%87%e5%a6%99%e5%86%92%e9%99%a9.html">JOJO的奇妙冒险</a></li>

            <li><a title="后宫动漫" href="/catalog/?label=%e5%90%8e%e5%ae%ab" target="_self">后宫动漫</a></li>

            
          </ul>
        </nav>
      </div>
      <div class="nav3">
        <form method="get" name="search" action="/search" target="_self" role="search" onSubmit="return checkForm(title)">
          <input class="shinput" name="keyword" type="text" placeholder="请输入您想要搜索的动画">
          <input hidden="hidden" name="seaex" type="text" value="1" readonly="readonly" />
          <input type="submit" value="搜索" class="searchbtn"></form>
      </div>
    </div>
</header>
  



        
        <div class="container clearfix">

          <div class="mbx">
            <a href="/">首页</a>>>
            <a href="/catalog/">动画连载</a>>> 黄金神威 第三季</div>
          <div class="sidebar-left">
            <div class=" normal-wai1">
              <div class="normal-inside">
                <div class="anime-img">
                  <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H24dc2c3df92641148f98f606e798edbcA.jpg" alt="黄金神威 第三季"></div>
                <div class="normal-nei1 adjs">


                  <div class="donghua_pf" id="main2">
                    <div class="pf">
                      <div class="pf3" id="avgscore">
                        <script>[29, 137.5, 4.741379310344827, 5.0, 0]</script>
                      </div>
                      <div class="stars" id="avgstar"></div>
                      <div class="pf1">评分:</div>
                      <div class="stars" id="stars"></div>
                    </div>
                    <div class="pf2">我的评分:</div>
                  </div>
                  <script type="text/javascript" src="/yxsf/js/yx_yxpf.js?ver=202011300081" type="text/javascript"></script>
  

                </div>
                <div class="normal-nei1 dhxx anime_info">
                  <h2>动画信息</h2>

                  
    <p>地区：<a href="/catalog/?region=%E6%97%A5%E6%9C%AC">日本</a></p>
    <p>动画种类：<a href="/catalog/?genre=TV">TV</a></p>
    <p>动画名称：<span style="color:#a7116f;">黄金神威 第三季</span></p>
    <p>原版名称：ゴールデンカムイ 第3期</p>
    <p>其它名称：暂无</p>
    <p>原作：野田サトル</p>
    <p>制作公司：Genostudio</p>
    <p>首播时间：2020-10-05</p>
    <p>播放状态：<a href="/catalog/?status=%E5%AE%8C%E7%BB%93">完结</a></p>
    <p>剧情类型：冒险 悬疑 战斗</p>
    <p>标签：<a href="/catalog/?label=%E5%86%92%E9%99%A9">冒险</a>&nbsp;<a href="/catalog/?label=%E6%82%AC%E7%96%91">悬疑</a>&nbsp;<a href="/catalog/?label=%E6%88%98%E6%96%97">战斗</a>&nbsp;</p>
    <p>资源类型：</p>
    <p>更新时间：2020-12-22 02:54:23</p>
    <p>系列：<a href="/family/%E9%BB%84%E9%87%91%E7%A5%9E%E5%A8%81.html">黄金神威</a></p>
    <p style="word-break:break-all;">官方网站：<a rel="nofollow" href="http://kamuy-anime.com/" target="_blank">http://kamuy-anime.com/</a></p>
    

                  <div id="nodiv">相关动画：
                    <ul class="id_inner">
                      
                      
        <li class="like">
            <a title="黄金神威 第二季 [2018-10-08]" href="/anime/20180163.html" target="_self">黄金神威 第二季</a> [2018-10-08]
        </li>
        
        <li class="like">
            <a title="黄金神威 [2018-04-09]" href="/anime/20180089.html" target="_self">黄金神威</a> [2018-04-09]
        </li>
        
        <li class="like">
            <a title="黄金神威OAD [2018-09-19]" href="/anime/20180263.html" target="_self">黄金神威OAD</a> [2018-09-19]
        </li>
        

                    </ul>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="adv4">
              <!--新番专题-->
            </div>

            <div class="side-update normal-wai">
              <div class="hd">
                <h2>233推荐</h2></div>
              <div class="normal-nei">
                <ul class="item-update item-update1 item-update2">

                  
        <li>
            <em>
                <a title="蔚蓝反射 澪" href="/anime/20210104.html" target="_self">蔚蓝反射 澪</a></em>
            <span class="anew">
                <a title="蔚蓝反射 澪" href="/anime/20210104.html" target="_self">第24话</a></span>
        </li>
        
        <li>
            <em>
                <a title="PROMARE" href="/anime/20190087.html" target="_self">PROMARE</a></em>
            <span class="anew">
                <a title="PROMARE" href="/anime/20190087.html" target="_self">[全集]</a></span>
        </li>
        
        <li>
            <em>
                <a title="美妙天堂 第二季" href="/anime/20150129.html" target="_self">美妙天堂 第二季</a></em>
            <span class="anew">
                <a title="美妙天堂 第二季" href="/anime/20150129.html" target="_self">[TV 39-89]</a></span>
        </li>
        
        <li>
            <em>
                <a title="Fate/stay night -UBW-" href="/anime/20140163.html" target="_self">Fate/stay night -UBW-</a></em>
            <span class="anew">
                <a title="Fate/stay night -UBW-" href="/anime/20140163.html" target="_self">[TV 00-12]</a></span>
        </li>
        
        <li>
            <em>
                <a title="强袭魔女" href="/anime/20080001.html" target="_self">强袭魔女</a></em>
            <span class="anew">
                <a title="强袭魔女" href="/anime/20080001.html" target="_self">[TV 01-12+OVA+SP]</a></span>
        </li>
        
        <li>
            <em>
                <a title="To LOVE Darkness OVA" href="/anime/20130095.html" target="_self">To LOVE Darkness OVA</a></em>
            <span class="anew">
                <a title="To LOVE Darkness OVA" href="/anime/20130095.html" target="_self">[OAD 01-10]</a></span>
        </li>
        
        <li>
            <em>
                <a title="神无月的巫女" href="/anime/20040012.html" target="_self">神无月的巫女</a></em>
            <span class="anew">
                <a title="神无月的巫女" href="/anime/20040012.html" target="_self">[DVD 01-12]</a></span>
        </li>
        
        <li>
            <em>
                <a title="IDOLY PRIDE" href="/anime/20200062.html" target="_self">IDOLY PRIDE</a></em>
            <span class="anew">
                <a title="IDOLY PRIDE" href="/anime/20200062.html" target="_self">[TV 01-12]</a></span>
        </li>
        
        <li>
            <em>
                <a title="魔法少女伊莉雅" href="/anime/20130001.html" target="_self">魔法少女伊莉雅</a></em>
            <span class="anew">
                <a title="魔法少女伊莉雅" href="/anime/20130001.html" target="_self">[TV 01-10+OVA]</a></span>
        </li>
        
        <li>
            <em>
                <a title="排球少年 第四季" href="/anime/20200055.html" target="_self">排球少年 第四季</a></em>
            <span class="anew">
                <a title="排球少年 第四季" href="/anime/20200055.html" target="_self">[TV 01-25]</a></span>
        </li>
        
        <li>
            <em>
                <a title="异世界魔王与召唤少女的奴隶魔术 第二季" href="/anime/20210101.html" target="_self">异世界魔王与召唤少女的奴隶魔术 第二季</a></em>
            <span class="anew">
                <a title="异世界魔王与召唤少女的奴隶魔术 第二季" href="/anime/20210101.html" target="_self">第10集(完结)</a></span>
        </li>
        
        <li>
            <em>
                <a title="白箱" href="/anime/20140091.html" target="_self">白箱</a></em>
            <span class="anew">
                <a title="白箱" href="/anime/20140091.html" target="_self">[TV 01-24+OVA]</a></span>
        </li>
        
        <li>
            <em>
                <a title="琴浦小姐" href="/anime/20130070.html" target="_self">琴浦小姐</a></em>
            <span class="anew">
                <a title="琴浦小姐" href="/anime/20130070.html" target="_self">[TV 01-12]</a></span>
        </li>
        
        <li>
            <em>
                <a title="便当" href="/anime/20110023.html" target="_self">便当</a></em>
            <span class="anew">
                <a title="便当" href="/anime/20110023.html" target="_self">[TV 01-12]</a></span>
        </li>
        
        <li>
            <em>
                <a title="来自深渊" href="/anime/20170051.html" target="_self">来自深渊</a></em>
            <span class="anew">
                <a title="来自深渊" href="/anime/20170051.html" target="_self">[TV 01-13]</a></span>
        </li>
        
        <li>
            <em>
                <a title="战斗员派遣中！" href="/anime/20210080.html" target="_self">战斗员派遣中！</a></em>
            <span class="anew">
                <a title="战斗员派遣中！" href="/anime/20210080.html" target="_self">[TV 01-12]</a></span>
        </li>
        
        <li>
            <em>
                <a title="青春期笨蛋不做兔女郎学姐的梦" href="/anime/20180213.html" target="_self">青春期笨蛋不做兔女郎学姐的梦</a></em>
            <span class="anew">
                <a title="青春期笨蛋不做兔女郎学姐的梦" href="/anime/20180213.html" target="_self">[TV 01-13]</a></span>
        </li>
        
        <li>
            <em>
                <a title="弹丸论破 希望学园与绝望高中生" href="/anime/20130002.html" target="_self">弹丸论破 希望学园与绝望高中生</a></em>
            <span class="anew">
                <a title="弹丸论破 希望学园与绝望高中生" href="/anime/20130002.html" target="_self">[TV 01-13]</a></span>
        </li>
        
        <li>
            <em>
                <a title="樱花任务" href="/anime/20170028.html" target="_self">樱花任务</a></em>
            <span class="anew">
                <a title="樱花任务" href="/anime/20170028.html" target="_self">[TV 01-25]</a></span>
        </li>
        
        <li>
            <em>
                <a title="警视厅 特务部 特殊凶恶犯对策室 第七课" href="/anime/20190217.html" target="_self">警视厅 特务部 特殊凶恶犯对策室 第七课</a></em>
            <span class="anew">
                <a title="警视厅 特务部 特殊凶恶犯对策室 第七课" href="/anime/20190217.html" target="_self">[TV 01-13]</a></span>
        </li>
        
                  
                </ul>
                <div style="clear:both;"></div>
              </div>
            </div>
          </div>
          <div class="main-right">
            <section>
              <div class="neirong">
                <div class="normal-nei2">
                  <div class="info">
                    <div class="info0">
                      <h1 class="h1-title">黄金神威 第三季</h1>
                    </div>

                    <div class="info1">
                      <ul class="info1-left" style="white-space:nowrap;">
                        <li>
                          <span>更新至</span>
                          <p style="width:7em;">[TV 01-12+SP]</p>
                        </li>

                        <li>
                          <span>播放状态</span>
                          <p>完结 <font color="#C66"></font></p>
                        </li>
                        <li>
                          <span>最后更新</span>
                          <p>2020-12-22 02:54:23</p>
                        </li>
                      </ul>
                      <ul class="info1-right">
                        <li>
                          <div class="a1">
                            <a href="#report_section" target="_self">资源报错</a></div>
                        </li>
                        <li>
                          <div class="a2">
                            <a href="#report_section" target="_self">动漫求源</a></div>
                        </li>
                        <li>
                          <div class="a3">
                            <a href="javascript:void(0);" onclick="AddFavorite('233动漫 - 黄金神威 第三季',location.href)" target="_self">加入收藏</a></div>
                        </li>
                      </ul>
                      <div class="bdsharebuttonbox">
                        <a href="#" class="bds_fbook" data-cmd="fbook" title="分享到Facebook"></a>
                        <a href="#" class="bds_twi" data-cmd="twi" title="分享到Twitter"></a>
                        <a href="#" class="bds_tieba" data-cmd="tieba" title="分享到百度贴吧"></a>
                        <a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a>
                        <a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博"></a>
                        <a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a>
                      </div>
                      <script>window._bd_share_config = {
                          "common": {
                            "bdSnsKey": {},
                            "bdText": "",
                            "bdMini": "2",
                            "bdMiniList": false,
                            "bdPic": "",
                            "bdStyle": "0",
                            "bdSize": "16"
                          },
                          "share": {}
                        };
                        with(document) 0[(getElementsByTagName('head')[0] || body).appendChild(createElement('script')).src = '/yxsf/static/api/js/share.js?ver=202011300081'];</script>
                      <div style="clear:both;"></div>
                    </div>
                    <div id="box" class="info2">
                      <p>
                        <strong>简介：</strong>

                        


          
          电视动画「黄金神威」第3季第2弹PV公开，片头曲 「Grey」与片尾曲「融雪」分别由 FOMARE 和 THE SIXTH LIE 演唱。该作将从10月5日起播出。
杉元佐一为了得到大量的黄金，来到了昔日淘金热潮盛行的北海道。机缘巧合下他得知了隐藏著阿依努人庞大财宝的线索......在充满威严的大自然中，和许多凶恶的死刑犯、以及爱奴少女相遇，寻找黄金的生存竞争正式开幕!!!
         





                      </p>
                    </div>
                  </div>

                  <div class="adv2">
                  </div>

                  <div style="clear:both;"></div>
                </div>
              </div>
            </section>

            
            <section>
              <div class="neirong1 t">
                <div class="normal-nei3">
                  <div class="ol-start">在线播放</div>
                  <div class="ol-select" id="zx_">
                    <ul>
                      <li id='zx_1' class="hoverzx" onclick="a:HoverLizx(1)">
                        <div class="qita"></div>线路Ⅰ</li>
                      <li id='zx_2' class="normalzx" onclick="b:HoverLizx(2)">
                        <div class="qita"></div>线路Ⅱ</li>
                      <li id='zx_3' class="normalzx" onclick="c:HoverLizx(3)">
                        <div class="qita"></div>线路Ⅲ</li>
                      <li id='zx_4' class="normalzx" onclick="d:HoverLizx(4)">
                        <div class="qita"></div>线路Ⅳ</li>
                        
                    </ul>
                  </div>
                  <div class="play-px">
                    <a href="javascript:;" onclick="changeorder(this,1)" target="_self" class="">
                      <em class="desc"></em>升序排序</a>
                    <a href="javascript:;" class="p-hide" onclick="changeorder(this,0)" target="_self">
                      <em class="asc"></em>降序排序</a>
                  </div>

                  
        <div class="ol-content zxdis" id='tzx_01'>
            <ul class="eplist-eppic">
                
        <li>
            <a href="/play/20200310-0-0.html" title="PV2" target="_self">
                <img referrerpolicy="no-referrer" src="//tvax3.sinaimg.cn/large/6e6880degy1gipbxxv0ekj2074040aa5.jpg" alt="PV2">
                <p>PV2</p>
            </a>
        </li>
        
            </ul>
        </div>
        
        <div class="ol-content zxundis" id='tzx_02'>
            <ul class="eplist-eppic">
                
        <li>
            <a href="/play/20200310-1-0.html" title="第01集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H01b972ee52fe4665857f7dc999fb2f2aq.jpg" alt="第01集">
                <p>第01集</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-1-1.html" title="第02集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/He173fb8107de4663b17994da8e695fffq.jpg" alt="第02集">
                <p>第02集</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-1-2.html" title="第03集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H11266323de444d0a86087dce39c763e1Y.jpg" alt="第03集">
                <p>第03集</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-1-3.html" title="第04集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/He47ce359abab4f6d99111377a59029a1x.jpg" alt="第04集">
                <p>第04集</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-1-4.html" title="第05集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H95fc33aeb46b49488dba430a90d57733z.jpg" alt="第05集">
                <p>第05集</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-1-5.html" title="第06集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H86860a487d6a46d694e43c8f679a7e31l.jpg" alt="第06集">
                <p>第06集</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-1-6.html" title="第07集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H8231625484dc44b19367da7e3219935au.jpg" alt="第07集">
                <p>第07集</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-1-7.html" title="第08集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H4771f7cdd0fb4b408b25524c2b869f3fH.jpg" alt="第08集">
                <p>第08集</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-1-8.html" title="第09集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/Hd8e359538f8b4d3d819d2a3fd2bbaf9eM.jpg" alt="第09集">
                <p>第09集</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-1-9.html" title="第10集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/Hbc442194658a455da6848a37fe1213e6P.jpg" alt="第10集">
                <p>第10集</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-1-10.html" title="第11集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H840e86139a944350889f19789275e745s.jpg" alt="第11集">
                <p>第11集</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-1-11.html" title="第12集" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H8e1a6753fe064d2b8f3c2d1aa42de613N.jpg" alt="第12集">
                <p>第12集</p>
            </a>
        </li>
        
            </ul>
        </div>
        
        <div class="ol-content zxundis" id='tzx_03'>
            <ul class="eplist-eppic">
                
        <li>
            <a href="/play/20200310-2-0.html" title="第01话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H01b972ee52fe4665857f7dc999fb2f2aq.jpg" alt="第01话 720P">
                <p>第01话 720P</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-2-1.html" title="第02话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/He173fb8107de4663b17994da8e695fffq.jpg" alt="第02话 720P">
                <p>第02话 720P</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-2-2.html" title="第03话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H11266323de444d0a86087dce39c763e1Y.jpg" alt="第03话 720P">
                <p>第03话 720P</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-2-3.html" title="第04话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/He47ce359abab4f6d99111377a59029a1x.jpg" alt="第04话 720P">
                <p>第04话 720P</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-2-4.html" title="第05话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H95fc33aeb46b49488dba430a90d57733z.jpg" alt="第05话 720P">
                <p>第05话 720P</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-2-5.html" title="第06话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H86860a487d6a46d694e43c8f679a7e31l.jpg" alt="第06话 720P">
                <p>第06话 720P</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-2-6.html" title="第07话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H8231625484dc44b19367da7e3219935au.jpg" alt="第07话 720P">
                <p>第07话 720P</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-2-7.html" title="第08话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H4771f7cdd0fb4b408b25524c2b869f3fH.jpg" alt="第08话 720P">
                <p>第08话 720P</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-2-8.html" title="第09话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/Hd8e359538f8b4d3d819d2a3fd2bbaf9eM.jpg" alt="第09话 720P">
                <p>第09话 720P</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-2-9.html" title="第10话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/Hbc442194658a455da6848a37fe1213e6P.jpg" alt="第10话 720P">
                <p>第10话 720P</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-2-10.html" title="第11话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H840e86139a944350889f19789275e745s.jpg" alt="第11话 720P">
                <p>第11话 720P</p>
            </a>
        </li>
        
        <li>
            <a href="/play/20200310-2-11.html" title="第12话 720P" target="_self">
                <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H8e1a6753fe064d2b8f3c2d1aa42de613N.jpg" alt="第12话 720P">
                <p>第12话 720P</p>
            </a>
        </li>
        
            </ul>
        </div>
        
        <div class="ol-content zxundis" id='tzx_04'>
            <ul class="eplist-normal">
                
            </ul>
        </div>
        

                </div>
              </div>
              <script id="DEF_PLAYINDEX">1</script>
              <script>
                __detail_hide_emptyplay();
              </script>

            </section>

            <!--下载-->
            <section id="dm-down">
              <div class="neirong1 t">
                <div class="normal-nei3">
                  <div id="down-start" class="down-start">动漫下载</div>
                  <div class="down-select" id="xz_">
                    <ul>
                      <li id='xz_1' class="hoverxz" onclick="a:HoverLixz(1)">网盘下载</li>
                      <li id='xz_2' class="normalxz" onclick="b:HoverLixz(2)"></li>
                    </ul>
                  </div>
                  <div class="down-px">
                    <a href="javascript:;" onclick="changeorder1(this,1)" target="_self" class="">
                      <em class="desc"></em>升序排序</a>
                    <a href="javascript:;" class="p-hide" onclick="changeorder1(this,0)" target="_self">
                      <em class="asc"></em>降序排序</a>
                  </div>
                  <div class="down-content xzdis" id='txz_01'>
                    <ul>
                      
        <li style="width:auto!important;">
            <a rel="nofollow" href="//www.yayashare.com/bdpan/share-20200310-0.html" target="_blank">
                <span>[TV 01-12+SP 720P]</span></a>
        </li>
        
                    </ul>
                  </div>
                  <div class="down-content xzundis" id='txz_02'>
                    <ul>
                      
        <li style="width:auto!important;">
            <a rel="nofollow" href="//www.yayashare.com/bdpan/share-20200310-0.html" target="_blank">
                <span>[TV 01-12+SP 720P]</span></a>
        </li>
        
                      
                    </ul>
                  </div>
                </div>
              </div>
            </section>

            <section id="report_section">
              <div class="neirong1 t">
                <div class="normal-nei3">
                  <div class="down-start">资源报错</div>
                  <div class="cai" style="padding-left:2.8%;">
                    
    <div class="report_div">
        <form id="report_form" action="/report" method="GET">
            <div>
                <input id="report_aid" type="hidden" name="animeid" value="">
                <label>
                    <input type="checkbox" name="link_invalid" value="1">链接失效</label>
                <label>
                    <input type="checkbox" name="bad_quality" value="1">资源质量差</label>
                <label>
                    <input type="checkbox" name="some_missing" value="1">集数缺失</label>
                <label>
                    <input type="checkbox" name="other" value="1">其他</label>
                <input name="oter_text" placeholder="请告诉DM233详细情况~~" wrap="SOFT" spellcheck="0" autocapitalize="off" autocomplete="off" autocorrect="off">
                <input class="nbutton" type="submit" value="提交"></div>
        </form>
        <script>var AID = window.location.href.replace(/.*\/anime\/(\d{8})\.html.*/, '$1');
            if (AID.length != 8) {
                AID = window.location.href.replace(/.*\/play\/(\d{8})-\d+?-\d+?\.html.*/, '$1');
            }
            $('#report_aid').attr('value', AID);

            /////////////////
            $('#report_form').on('submit',
            function() {
                registPost();
                event.preventDefault(); //阻止form表单默认提交
            });

            ///////////////////
            function registPost() {
                $.ajax({
                    type: "get",
                    url: "/report?" + $('#report_form').serialize(),
                }).success(function(message) {
                    alert(message);
                }).fail(function(err) {
                    alert('未知错误');
                });
            }</script>
    </div>
    
                  </div>
                </div>
              </div>
            </section>

            
    <section>
        <div class="neirong1 t">
            <div class="normal-nei3">
                <div class="down-start">相关资讯</div>
                <div class="xgyd mt1 clearfix">
                    <ul>
    
        <li>
            <a href="/article/e86915090f75e3b3.html" title="山森三香绘制「黄金神威」尾形百之助插图公开">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="https://pic.rmb.bdstatic.com/bjh/60b89e522016d51f72fd05cf24f5b832.jpeg" alt="山森三香绘制「黄金神威」尾形百之助插图公开">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/e86915090f75e3b3.html">山森三香绘制「黄金神威」尾形百之助插图公开</a></div>
        </li>
        
        <li>
            <a href="/article/d176200a5429a6b6.html" title="TV动画「黄金神威」第3季追加新角色">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="//sc02.alicdn.com/kf/Haf527bce499749f8aac122d7b87c994ab.jpg" alt="TV动画「黄金神威」第3季追加新角色">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/d176200a5429a6b6.html">TV动画「黄金神威」第3季追加新角色</a></div>
        </li>
        
        <li>
            <a href="/article/d9fe0327e7ebf6a5.html" title="「黄金神威」推出首部官方FanBook">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="//sc02.alicdn.com/kf/H57831299fd404fc9a18fbc5e34950483e.jpg" alt="「黄金神威」推出首部官方FanBook">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/d9fe0327e7ebf6a5.html">「黄金神威」推出首部官方FanBook</a></div>
        </li>
        
        <li>
            <a href="/article/18ff499fbc16e03d.html" title="TV动画「黄金神威」第三季公开第2弹视觉图">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="//tvax3.sinaimg.cn/large/6e6880degy1giqc28mtxpj209p05j0t9.jpg" alt="TV动画「黄金神威」第三季公开第2弹视觉图">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/18ff499fbc16e03d.html">TV动画「黄金神威」第三季公开第2弹视觉图</a></div>
        </li>
        
        <li>
            <a href="/article/93d690a938c3fdec.html" title="TV动画「黄金神威」第3季第2弹PV公开">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="//tvax3.sinaimg.cn/large/6b9238e5gy1gijh63eqz7j209p05jt9h.jpg" alt="TV动画「黄金神威」第3季第2弹PV公开">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/93d690a938c3fdec.html">TV动画「黄金神威」第3季第2弹PV公开</a></div>
        </li>
        
        <li>
            <a href="/article/3dd7187f3f24931f.html" title="「黄金神威」第三季追加声优三宅健太">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="//tvax3.sinaimg.cn/large/6b9238e5gy1gi4du38qjsj20ih0b40v7.jpg" alt="「黄金神威」第三季追加声优三宅健太">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/3dd7187f3f24931f.html">「黄金神威」第三季追加声优三宅健太</a></div>
        </li>
        
        <li>
            <a href="/article/beceb39f1f62d4bd.html" title="稻川淳二讲述怪谈风格的「黄金神威」">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="//tvax3.sinaimg.cn/large/6e6880degy1gfxtx26yr0j209q077q73.jpg" alt="稻川淳二讲述怪谈风格的「黄金神威」">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/beceb39f1f62d4bd.html">稻川淳二讲述怪谈风格的「黄金神威」</a></div>
        </li>
        
        <li>
            <a href="/article/95258f026a4e47be.html" title="「黄金神威」动画第三季视觉图公开">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="//tvax3.sinaimg.cn/large/6e6880degy1gfxtwp4db2j209q05kacq.jpg" alt="「黄金神威」动画第三季视觉图公开">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/95258f026a4e47be.html">「黄金神威」动画第三季视觉图公开</a></div>
        </li>
        
        <li>
            <a href="/article/22c78b168a1ad8db.html" title="「黄金神威」第三期PV第一弹公开，动画10月开播">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="//tvax3.sinaimg.cn/large/6e6880degy1gcw3y89cnbj209q05jgo0.jpg" alt="「黄金神威」第三期PV第一弹公开，动画10月开播">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/22c78b168a1ad8db.html">「黄金神威」第三期PV第一弹公开，动画10月开播</a></div>
        </li>
        
        <li>
            <a href="/article/b5478080f0ea60e3.html" title="「黄金神威」同捆版单行本23卷附带支遁动物记篇动画">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="//tvax3.sinaimg.cn/large/6e6880degy1gcri0y47tsj209q05jq5y.jpg" alt="「黄金神威」同捆版单行本23卷附带支遁动物记篇动画">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/b5478080f0ea60e3.html">「黄金神威」同捆版单行本23卷附带支遁动物记篇动画</a></div>
        </li>
        
        <li>
            <a href="/article/fc5e4bb847217677.html" title="「黄金神威」开放特设网站多主题阅读板块">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="//tvax3.sinaimg.cn/large/6e6880degy1gc2isuo4i9j20fu0900y1.jpg" alt="「黄金神威」开放特设网站多主题阅读板块">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/fc5e4bb847217677.html">「黄金神威」开放特设网站多主题阅读板块</a></div>
        </li>
        
        <li>
            <a href="/article/e7759910163b2e07.html" title="再等三个月！「黄金神威」第二季动画10月播出！">
                <div class="picsize">
                    <img referrerpolicy="no-referrer" class="zsypic" src="//tvax3.sinaimg.cn/large/6e6880degy1g64be6dtgnj209q05jdhi.jpg" alt="再等三个月！「黄金神威」第二季动画10月播出！">
                    <label class="zhonglei">资讯</label></div>
            </a>
            <div class="xgyd-title">
                <a href="/article/e7759910163b2e07.html">再等三个月！「黄金神威」第二季动画10月播出！</a></div>
        </li>
        
                    </ul>
                </div>
            </div>
        </div>
    </section>
    

            
            <section id="cai_nodiv">
              <div class="neirong1 t">
                <div class="normal-nei3">
                  <div class="down-start">猜你喜欢</div>
                  <div class="cai">
                    <div class="root clearfix sec2 mb0">
                      <div class="dhnew adj">
                        <ul class="cai_inner">

                          
        <li>
            <p>
                <a title="BEM" href="/anime/20190186.html" target="_self">
                    <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/Ha1ce31d6c6964f3bb439187ae92e58b1I.jpg" alt="BEM">
                    <p>BEM</p>
                </a>
            </p>
        </li>
        
        <li>
            <p>
                <a title="怪物弹珠新系列 诺亚 方舟的救世主" href="/anime/20190194.html" target="_self">
                    <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H4d30bb4967cc439e80208a5086f7e732R.jpg" alt="怪物弹珠新系列 诺亚 方舟的救世主">
                    <p>怪物弹珠新系列 诺亚 方舟的救世主</p>
                </a>
            </p>
        </li>
        
        <li>
            <p>
                <a title="我不是说了能力要平均值么！" href="/anime/20190203.html" target="_self">
                    <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/H7297ca94b8c94507832bb93aea606fc2n.jpg" alt="我不是说了能力要平均值么！">
                    <p>我不是说了能力要平均值么！</p>
                </a>
            </p>
        </li>
        
        <li>
            <p>
                <a title="虚空魔法使 第二季" href="/anime/20190204.html" target="_self">
                    <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/Hb3c7acfd3e8945f48237a96d9c39ad47d.jpg" alt="虚空魔法使 第二季">
                    <p>虚空魔法使 第二季</p>
                </a>
            </p>
        </li>
        
        <li>
            <p>
                <a title="Fairy gone 第二季" href="/anime/20190207.html" target="_self">
                    <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/Ha41cc5d009e347a28d2afbbf9d19283ao.jpg" alt="Fairy gone 第二季">
                    <p>Fairy gone 第二季</p>
                </a>
            </p>
        </li>
        
        <li>
            <p>
                <a title="战×恋" href="/anime/20190213.html" target="_self">
                    <img referrerpolicy="no-referrer" src="https://sc04.alicdn.com/kf/Hc9780c9838874c7f87d53ea75e5b9e0bT.jpg" alt="战×恋">
                    <p>战×恋</p>
                </a>
            </p>
        </li>
        

                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>          
            </section>
 

            <section id="dm-comment">
              <div class="neirong1 t">
                <div class="normal-nei3">
                  <div class="down-start">评论浏览</div>
                  <div class="pinglun">

                    <div id="container" data-id="city" style="position: relative;">
                      <div id="wrapper" class="" data-version="">
                        <div class="emotion-widget"></div>
                        <div id="login">
                          <ul id="login-account">
                            <li id="login-img">
                              <button type="button" id="login-img-btn" data-path="c_profile" title="头像">
                                <img referrerpolicy="no-referrer" src="" alt="头像"></button>
                            </li>
                            <li id="login-type">
                              <button type="button" id="login-type-btn" data-path="c_profile" title="login type">
                                <span class="text-indent i-p-twitter">login type</span></button>
                            </li>
                            <li id="login-name">
                              <button type="button" id="login-name-btn" data-target="#login-layer">
                                <span id="login-name-text">游客</span>
                                <i class="i-drop-b"></i>
                              </button>
                            </li>

                          </ul>
                        </div>
                        <div id="fake-form" class="hide">
                          <textarea id="fake-content" placeholder="撰写评论"></textarea>
                          <button type="button" class="fake-write-btn">
                            <span>发布</span></button>
                        </div>
                        <div id="wf" class="wf-login-enable">
                          <div id="wf-form" class="wf-form outline-qq">
                            <div class="wf-content-wrapper">
                              <label for="wf-content">评论输入领域</label>
                              <textarea id="wf-content" placeholder="撰写评论"></textarea>
                              <script>
                                $('#wf-content').on('keyup', function(){
                                  this.scrollTop = 'auto';
                                  this.style.height = this.scrollHeight + 'px';
                                });
                              </script>
                            </div>
                            <div class="wf-attach-wrapper wf-bottom-wrapper">
                              <div class="attach-drag-wrapper hide">
                                <div>
                                  <span class="attach-drag-icon i-photo-drag-b"></span>
                                  <span class="attach-drag-guide">把照片拖拽到这里</span></div>
                              </div>
                              <div class="attach-image-wrapper"></div>
                              <div class="attach-scrap-wrapper"></div>
                            </div>
                            <div class="wf-function-wrapper">
                              <div class="wf-attach-function">
                                <div class="attach-photo-btn">
                                  <form action="/image/upload/" method="post" enctype="multipart/form-data">
                                    <div class="upload i-photo-b">
                                      <label for="lv_file_1" class="text-indent">添加照片</label>
                                      <input id="lv_file_1" type="file" name="lv_file" multiple=""></div>
                                  </form>
                                </div>
                              </div>
                              <div class="wf-sticker-function">
                                <button type="button" id="open-sticker-btn" class="open-sticker-btn i-sticker-b" data-name="wf">
                                  <span>open sticker</span></button>
                              </div>
                              <div id="wf-function" class="wf-function">
                                <button type="button" id="wf-write-btn" class="wf-write-btn">
                                  <span>发布</span></button>
                              </div>
                            </div>

                            <div id="emoji_frame" class="wf-sticker-wrapper" hidden="hidden"></div>

                          </div>
                        </div>
                        <div id="strategies" class="sns-login-enable">
                          <div id="sns-login"></div>
                          <div id="guest"></div>
                        </div>
                        <div id="highlight"></div>
                        <div class="reply-count">
                          <div class="left">评论
                            <span class="count-text">0</span></div>
                          <div class="sort">

                          </div>
                        </div>
                        <div id="list" class=""></div>
                        <div id="comment_page" class="pagelist"></div>
                      </div>

                    </div>
                    

                    <script type="text/javascript" src="/yxsf/js/yx_comment.js?ver=202011300081"></script>
                    <script>
                      __comment_init();
                      __set_on_sendcomment();
                      __yx_show_comments_page();
                    </script>


                  </div>
                </div>
              </div>
            </section>
          </div>
          <!--20180319-->
          <div class="messagebox show-notice">
            <div id="info">
              <div class="tishi">提示：您访问的是转码页面，内容无法正常显示。请点此</div>
              <p class="tishi_p">
                <a class="messagebtn1" href="/">访问首页</a></p>
            </div>
          </div>
          <script>$('.messagebox').hide();</script>
          <script type="text/javascript" src="/yxsf/js/yx_fbx1.js?v=20190528"></script>
        </div>
      </div>
    </div>

    <div class="linkf">
      <div class="linkf-content">
        <div>
          <span>快速导航：</span>
          <ul>

              
        <li>
            <a title="海贼王" href="/anime/20000001.html">海贼王</a>
        </li>
        
        <li>
            <a title="银魂 (001-201)" href="/anime/20060011.html">银魂 (001-201)</a>
        </li>
        
        <li>
            <a title="博人传 火影忍者新时代" href="/anime/20170172.html">博人传 火影忍者新时代</a>
        </li>
        
        <li>
            <a title="妖精的尾巴 最终季" href="/anime/20180256.html">妖精的尾巴 最终季</a>
        </li>
        
        <li>
            <a title="名侦探柯南" href="/anime/20000005.html">名侦探柯南</a>
        </li>
        
        <li>
            <a title="一拳超人 第二季" href="/anime/20190086.html">一拳超人 第二季</a>
        </li>
        
        <li>
            <a title="JOJO的奇妙冒险 第一二部(幻影之血+战斗潮流)" href="/anime/20120075.html">JOJO的奇妙冒险 第一二部(幻影之血+战斗潮流)</a>
        </li>
        

          </ul>
        </div>
      </div>
    </div>
    <footer role="contentinfo">
      <div class="footer-content">
        <p>本站的
          <strong>日本动漫</strong>由网络第三方视频类网站收集，本站不提供任何视听上传服务，所有内容均来自视频分享站点所提供的公开引用资源。</p>
        <p>
          <small>© 2019 233动漫 . All Rights Reserved</small>
          <div style="display:none;">
 
          </div>
        </p>
      </div>
    </footer>

    <!-- ad1+1 -->
    <script src='//pc.jinrongwang.net/pc/couplet-tf.js' id="coupletid" data='s=5416'></script>
    <script src='//pc.jinrongwang.net/pc/rich-tf.js' id="richid" data='s=4609'></script>


    <script type="text/javascript" src="/yxsf/js/yx_arc.js?ver=202011300081" type="text/javascript"></script>
    <script type="text/javascript" src="/yxsf/js/yx_common.js" type="text/javascript"></script>


    
    <script src="https://aq.cppoc.com/c/83D6B6BD-9CB0-46FC-9AB5-9EDF963DF936.ap"></script>
    
    
    

  </body>

  
    <script type="text/javascript" src="https://s4.cnzz.com/z_stat.php?id=1280265608&web_id=1280265608"></script>
    
    


</html>



    '''
    r = detail_analysis(a)
    pass
