/* 莞促集团官网 · 交互脚本 */
(function () {
  'use strict';

  // 导航滚动态
  var nav = document.querySelector('.nav');
  function onScroll() {
    if (nav) nav.classList.toggle('scrolled', window.scrollY > 12);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // 移动端菜单
  var btn = document.querySelector('.menu-btn');
  var menu = document.querySelector('.nav-menu');
  if (btn && menu) {
    btn.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      btn.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        menu.classList.remove('open');
        btn.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // 当前导航高亮
  var page = document.body.getAttribute('data-page') || '';
  document.querySelectorAll('.nav-menu a[data-nav]').forEach(function (a) {
    if (a.getAttribute('data-nav') === page) {
      a.classList.add('active');
      a.setAttribute('aria-current', 'page');
    }
  });

  // 年份
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // 滚动出现
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && items.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('in');
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) {
      io.observe(el);
    });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // 咨询表单：以邮件方式唤起本地邮件客户端
  var form = document.getElementById('consult-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var subject = '官网业务咨询 · ' + (d.get('company') || d.get('name') || '合作意向');
      var body = [
        '姓名：' + (d.get('name') || ''),
        '单位：' + (d.get('company') || ''),
        '联系电话：' + (d.get('phone') || ''),
        '关注业务：' + (d.get('topic') || ''),
        '',
        '需求说明：',
        d.get('message') || ''
      ].join('\n');
      window.location.href = 'mailto:v@guancu.com?subject=' +
        encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      var tip = document.getElementById('form-tip');
      if (tip) tip.textContent = '已为您打开邮件客户端，发送后即有专人跟进。';
    });
  }
})();
