(function(e){var c=e.tools.overlay,a=e(window);
e.extend(c.conf,{start:{top:null,left:null},fadeInSpeed:"fast",zIndex:9999});
function d(g){var h=g.offset();
return{top:h.top,left:h.left}
}var f=function(r,q){var k=this.getOverlay(),o=this.getConf(),i=this.getTrigger(),s=this,t=k.outerWidth({margin:true}),m=k.data("img"),n=o.fixed?"fixed":"absolute";
if(!m){var l=k.css("backgroundImage");
if(!l){throw"background-image CSS property not set for overlay"
}l=l.slice(l.indexOf("(")+1,l.indexOf(")")).replace(/\"/g,"");
k.css("backgroundImage","none");
m=e('<img src="'+l+'"/>');
m.css({border:0,display:"none"}).width(t);
e("body").append(m);
k.data("img",m)
}var j=o.start.top||Math.round(a.height()/2),h=o.start.left||Math.round(a.width()/2);
if(i){var g=d(i);
j=g.top;
h=g.left
}if(o.fixed){j-=a.scrollTop();
h-=a.scrollLeft()
}else{}m.css({position:"absolute",top:j,left:h,width:i.width(),zIndex:o.zIndex}).show();
r.position=n;
k.css(r);
m.animate({top:r.top,left:r.left,width:t},o.speed,function(){k.css("zIndex",o.zIndex+1).fadeIn(o.fadeInSpeed,function(){if(s.isOpened()&&!e(this).index(k)){q.call()
}else{k.hide()
}})
}).css("position",n)
};
var b=function(g){var k=this.getOverlay().hide(),j=this.getConf(),i=this.getTrigger(),h=k.data("img"),l={top:j.start.top,left:j.start.left,width:0};
if(i){e.extend(l,d(i))
}if(j.fixed){h.css({position:"absolute"}).animate({top:"+="+a.scrollTop(),left:"+="+a.scrollLeft()},0)
}h.animate(l,j.closeSpeed,g)
};
c.addEffect("appleExtended",f,b)
})(jQuery);