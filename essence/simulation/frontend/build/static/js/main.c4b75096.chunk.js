(this.webpackJsonpsimulation=this.webpackJsonpsimulation||[]).push([[0],{33:function(e,t,n){e.exports=n(47)},46:function(e,t){},47:function(e,t,n){"use strict";n.r(t);var a=n(0),i=n.n(a),r=n(21),s=n.n(r),o=n(2),c=n(4),l=n(6),u=n(5),h=n(38)("variabelen"),y=function e(t){Object(o.a)(this,e),this.generateName=function(){return"Jon"},this.generateSkinTone=function(){return h()>=.5?"black":"white"},this.generateCrimes=function(){return h()>=.5},this.index=t.index,this.name=this.generateName(),this.skinTone=this.generateSkinTone(),this.guilty=this.generateCrimes(),this.control=void 0},d=n(1),f={circle:{transition:"all ease 1s",transformOrigin:"center"}},m=function(e){Object(l.a)(n,e);var t=Object(u.a)(n);function n(e){var a;return Object(o.a)(this,n),(a=t.call(this,e)).references={citizen:i.a.createRef()},a.state={xCoord:"".concat(Math.round(90*Math.random())+5,"%"),yCoord:"".concat(Math.round(90*Math.random())+5,"%")},a}return Object(c.a)(n,[{key:"componentDidMount",value:function(){this.animate()}},{key:"componentDidUpdate",value:function(){this.animate()}},{key:"animate",value:function(){switch(this.props.phase){case 1:this.animatePhase1();break;case 2:this.animatePhase2();break;default:this.animatePhase1()}}},{key:"animatePhase1",value:function(){var e=this.props,t=e.duration,n=e.index,a=e.skinTone,i=e.guilty,r=t/4,s=.75*r*(n/100),o=.25*r;"white"===a&&d.a(this.references.citizen.current).style("opacity",0).transition().delay(r).transition().delay(s).duration(o).style("opacity",.5),"black"===a&&d.a(this.references.citizen.current).style("opacity",0).transition().delay(2*r).transition().delay(s).duration(o).style("opacity",.5),i&&d.a(this.references.citizen.current).transition().delay(3*r).transition().delay(s).duration(2*o).style("stroke","#FF4262").attr("stroke-width",3).style("opacity",.5),d.a(this.references.citizen.current).transition().delay(t).duration(o).style("opacity",0)}},{key:"animatePhase2",value:function(){var e=this.props,t=e.skinTone,n=e.count,a=e.control,i=n%5,r="".concat("white"===t?21+5*i:65+5*i,"%"),s="".concat(5*Math.ceil(n/5)+15,"%");d.a(this.references.citizen.current).style("opacity",0),a&&d.a(this.references.citizen.current).transition().delay(700*n).duration(1e3).style("opacity",1).attr("cx",r).attr("cy",s)}},{key:"render",value:function(){var e=this.props.skinTone,t=this.state,n=t.xCoord,a=t.yCoord;return i.a.createElement("circle",{ref:this.references.citizen,style:f.circle,cx:n,cy:a,r:"10",stroke:"#16284A",fill:"white"===e?"white":"#16284A",strokeWidth:"1"})}}]),n}(i.a.PureComponent),p={text:{textAnchor:"middle",fontSize:"1.8em",fill:"#16284A",fontFamily:"Poppins",backgroundColor:"white"},text2:{textAnchor:"middle",fontSize:"1.2em",fill:"#16284A",fontFamily:"Poppins"},text3:{textAnchor:"middle",fontSize:"1.2em",fill:"#16284A",fontFamily:"Poppins"},text4:{textAnchor:"middle",fontSize:"1.2em",fill:"#16284A",fontFamily:"Poppins"}},x=function(e){Object(l.a)(n,e);var t=Object(u.a)(n);function n(e){var a;return Object(o.a)(this,n),(a=t.call(this,e)).references={text1:i.a.createRef(),text2:i.a.createRef(),text3:i.a.createRef(),text4:i.a.createRef()},a}return Object(c.a)(n,[{key:"componentDidMount",value:function(){this.animate()}},{key:"componentDidUpdate",value:function(){this.animate()}},{key:"animate",value:function(){switch(this.props.phase){case 1:this.animatePhase1();break;case 2:this.animatePhase2();break;default:this.animatePhase1()}}},{key:"animatePhase1",value:function(){var e=this.props.duration/4,t=.5*e,n=.25*e;d.a(this.references.text1.current).style("opacity",0).transition().duration(n).style("opacity",1).text("Een fictieve populatie van 100 mensen").transition().delay(t).duration(n).style("opacity",0).transition().duration(n).style("opacity",1).text("Sommigen zijn wit").transition().delay(t).duration(n).style("opacity",0).transition().duration(n).style("opacity",1).text("Sommigen zijn zwart").transition().delay(t).duration(n).style("opacity",0).transition().duration(n).style("opacity",1).text("Sommigen zijn crimineel").transition().delay(t).duration(n).style("opacity",0).transition().delay(t).duration(n).style("opacity",1).text('De politie controleert vaker in "zwarte" buurten...').transition().delay(t).duration(n).style("opacity",0).transition().duration(n).style("opacity",1).text("...\xe9n is bevooroordeeld.").transition().delay(t).duration(n).style("opacity",0)}},{key:"animatePhase2",value:function(){var e=this.props.duration/4,t=.5*e,n=.25*e;d.a(this.references.text2.current).style("opacity",0).transition().delay(2*t).duration(n).style("opacity",1).text("Dit zijn alle gecontroleerde mensen.").transition().delay(.8*t).duration(n).style("opacity",0).transition().duration(n).style("opacity",1).text("De politie telt het aantal criminelen van elke huidskleur.").transition().delay(.8*t).duration(n).style("opacity",0).transition().duration(n).style("opacity",1).text("Dit is de totale verdeling van criminelen per huidskleur:").transition().delay(.8*t).duration(n).style("opacity",0),d.a(this.references.text3.current).style("opacity",0).transition().delay(8*t).duration(n).style("opacity",1).text("Percentage witte criminelen"),d.a(this.references.text4.current).style("opacity",0).transition().delay(8*t).duration(n).style("opacity",1).text("Percentage zwarte criminelen")}},{key:"render",value:function(){return i.a.createElement("g",null,i.a.createElement("text",{ref:this.references.text1,style:p.text,className:"narrator",x:"50%",y:"50%"}),i.a.createElement("text",{ref:this.references.text2,style:p.text2,className:"narrator",x:"50%",y:"50%"}),i.a.createElement("text",{ref:this.references.text3,style:p.text3,className:"narrator",x:"26%",y:"85%"}),i.a.createElement("text",{ref:this.references.text4,style:p.text4,className:"narrator",x:"81%",y:"85%"}))}}]),n}(i.a.PureComponent),k={text:{textAnchor:"middle",fontSize:"1.5em",fill:"#16284A",fontFamily:"Poppins"}},v=function(e){Object(l.a)(n,e);var t=Object(u.a)(n);function n(e){var a;return Object(o.a)(this,n),(a=t.call(this,e)).references={title1:i.a.createRef(),title2:i.a.createRef()},a}return Object(c.a)(n,[{key:"componentDidMount",value:function(){this.animate()}},{key:"componentDidUpdate",value:function(){this.animate()}},{key:"animate",value:function(){switch(this.props.phase){case 1:this.animatePhase1();break;case 2:this.animatePhase2();break;default:this.animatePhase1()}}},{key:"animatePhase1",value:function(){d.a(this.references.title1.current).style("opacity",0),d.a(this.references.title2.current).style("opacity",0)}},{key:"animatePhase2",value:function(){var e=this.props.duration/4,t=.5*e,n=.25*e;d.a(this.references.title1.current).transition().delay(t).duration(n).style("opacity",1),d.a(this.references.title2.current).transition().delay(t).duration(n).style("opacity",1)}},{key:"render",value:function(){return i.a.createElement("g",null,i.a.createElement("text",{className:"title",ref:this.references.title1,x:"30%",y:"10%",width:"50%",height:"10%",style:k.text},"Witte mensen"),i.a.createElement("text",{className:"title",ref:this.references.title2,x:"75%",y:"10%",width:"50%",height:"10%",style:k.text},"Zwarte mensen"))}}]),n}(i.a.PureComponent),g={bar:{transform:"translate(6%, 0) rotate(180deg)"},barContainer1:{transform:"translate(46%, 90%)"},barContainer2:{transform:"translate(54%, 90%)"},text:{fontFamily:"Poppins",fontSize:"1em",textAnchor:"middle",fill:"white",transform:"translate(3%, 0)"},text2:{fontFamily:"Poppins",fontSize:"1em",textAnchor:"middle",fill:"#16284A",transform:"translate(3%, 0)"}},b=function(e){Object(l.a)(n,e);var t=Object(u.a)(n);function n(e){var a;return Object(o.a)(this,n),(a=t.call(this,e)).references={stats1:i.a.createRef(),stats2:i.a.createRef(),text1:i.a.createRef(),text2:i.a.createRef(),text3:i.a.createRef(),text4:i.a.createRef()},a}return Object(c.a)(n,[{key:"componentDidMount",value:function(){this.animate()}},{key:"componentDidUpdate",value:function(){this.animate()}},{key:"animate",value:function(){switch(this.props.phase){case 1:this.animatePhase1();break;case 2:this.animatePhase2()}}},{key:"animatePhase1",value:function(){d.a(this.references.text1.current).style("opacity",0),d.a(this.references.text2.current).style("opacity",0),d.a(this.references.text3.current).style("opacity",0),d.a(this.references.text4.current).style("opacity",0)}},{key:"animatePhase2",value:function(){var e=this.props,t=e.duration,n=e.percentageWhite,a=e.percentageBlack,i=t/4,r=.5*i,s=.25*i;d.a(this.references.stats1.current).transition().delay(3*i).transition().delay(r).duration(s).attr("height","".concat(n,"%")),d.a(this.references.stats2.current).transition().delay(3*i).transition().delay(r).duration(s).attr("height","".concat(a,"%")),d.a(this.references.text1.current).transition().delay(3*i).transition().delay(r).duration(s).style("opacity",1),d.a(this.references.text2.current).transition().delay(3*i).transition().delay(r).duration(s).style("opacity",1),d.a(this.references.text3.current).transition().delay(3*i).transition().delay(r).duration(s).style("opacity",1),d.a(this.references.text4.current).transition().delay(3*i).transition().delay(r).duration(s).style("opacity",1)}},{key:"render",value:function(){return i.a.createElement("g",null,i.a.createElement("g",{style:g.barContainer1},i.a.createElement("rect",{ref:this.references.stats1,style:g.bar,x:"0",y:"0",width:"6%",height:"0",fill:"#2396CD",strokeWidth:"0"}),i.a.createElement("text",{ref:this.references.text1,x:"0",y:"-1%",style:g.text},Math.round(this.props.percentageWhite),"%")),i.a.createElement("g",{style:g.barContainer2},i.a.createElement("rect",{ref:this.references.stats2,style:g.bar,x:"0",y:"0",width:"6%",height:"0",fill:"#2396CD",strokeWidth:"0"}),i.a.createElement("text",{ref:this.references.text3,x:"0",y:"-1%",style:g.text},Math.round(this.props.percentageBlack),"%")))}}]),n}(i.a.PureComponent),P=function(e){Object(l.a)(n,e);var t=Object(u.a)(n);function n(e){var a;return Object(o.a)(this,n),(a=t.call(this,e)).citizenAmount=100,a.durationPhase1=15e3,a.durationPhase2=1e4,a.delayBetweenPhases=8e3,a.state={citizens:[],phase:1,duration:a.durationPhase1,percentageWhite:0,percentageBlack:0,maxHeight:null,maxWidth:null},a}return Object(c.a)(n,[{key:"componentDidMount",value:function(){this.setSize(),this.generatePopulation(),this.startPhaseCountdown()}},{key:"setSize",value:function(){console.log(window.innerWidth),window.innerWidth<768?this.setState({maxHeight:"250px",maxWidth:"400px"}):this.setState({maxHeight:"500px",maxWidth:"800px"})}},{key:"startPhaseCountdown",value:function(){var e=this,t=this.durationPhase1+this.delayBetweenPhases;setTimeout((function(){console.log(e.state.citizens);var t=e.state.citizens.filter((function(e){return e.control&&e.guilty&&"white"===e.skinTone})).length,n=e.state.citizens.filter((function(e){return e.control&&e.guilty&&"black"===e.skinTone})).length,a=e.state.citizens.filter((function(e){return e.control&&e.guilty})).length,i=t/a*100,r=n/a*100;e.setState({duration:e.durationPhase2,phase:2,percentageWhite:i,percentageBlack:r})}),t)}},{key:"generatePopulation",value:function(){for(var e=[],t=0;t<this.citizenAmount;t++)e.push(new y({index:t}));this.setState({citizens:e})}},{key:"renderCitizens",value:function(){var e=this.state,t=e.citizens,n=e.duration,a=e.phase,r=0,s=0;return t.map((function(e,t,o){var c=o[t-1];if("white"===e.skinTone){var l=function(){return Math.random()>=.8};e.control=l()}else void 0===c&&"black"===e.skinTone?(l=function(){return Math.random()>=.2},e.control=l()):"black"===c.skinTone&&"black"===e.skinTone?(l=function(){return Math.random()>=.1},e.control=l()):"white"===c.skinTone&&"black"===e.skinTone&&(l=function(){return Math.random()>=.2},e.control=l());return r="white"===e.skinTone&&e.control?r+1:r,s="black"===e.skinTone&&e.control?s+1:s,i.a.createElement(m,{key:e.index,index:e.index,duration:n,phase:a,skinTone:e.skinTone,guilty:e.guilty,name:e.name,count:"white"===e.skinTone?r:s,control:e.control})}))}},{key:"render",value:function(){var e=this.state,t=e.duration,n=e.phase,a=e.percentageBlack,r=e.percentageWhite,s=e.maxHeight,o=e.maxWidth,c=this.renderCitizens(),l={svg:{width:"100%",height:"100%",maxWidth:o,maxHeight:s,flex:1,textAlign:"center",verticalAlign:"middle",alignItems:"center",margin:0,padding:"1rem",boxSizing:"border-box"}};return console.log(this.state),i.a.createElement("svg",{style:l.svg,viewBox:"0 0 800 500"},c,i.a.createElement(x,{phase:n,duration:t}),i.a.createElement(v,{phase:n,duration:t}),i.a.createElement(b,{phase:n,duration:t,percentageWhite:r,percentageBlack:a}))}}]),n}(i.a.PureComponent),w=function(e){Object(l.a)(n,e);var t=Object(u.a)(n);function n(e){var a;return Object(o.a)(this,n),(a=t.call(this,e)).setSize=function(){window.innerWidth>768?a.setState({top:"480px",left:"48%"}):window.innerWidth<768&&a.setState({top:"250px",left:"42%"})},a.startSimulation=function(){a.setState({startSim:!0})},a.refresh=function(){a.setState({key:Math.random()})},a.state={startSim:!1,key:Math.random(),top:null,left:null},a}return Object(c.a)(n,[{key:"componentDidMount",value:function(){this.setSize()}},{key:"render",value:function(){var e=this,t=this.state,n=t.startSim,a=t.key,r=t.top,s={button:{display:"inline-block",border:"none",margin:"0",textDecoration:"none",background:"#145594",color:"#ffffff",fontFamily:"Poppins",fontSize:"1rem",textAlign:"center",position:"absolute",left:t.left,top:r}};return i.a.createElement("div",null,!n&&i.a.createElement("button",{onClick:function(){return e.startSimulation()}},"Start"),n&&i.a.createElement("button",{className:"refresh",style:s.button,onClick:function(){return e.refresh()}},"Refresh"),n&&i.a.createElement(P,{key:a}))}}]),n}(i.a.PureComponent);s.a.render(i.a.createElement(i.a.StrictMode,null,i.a.createElement(w,null)),document.getElementById("root"))}},[[33,1,2]]]);
//# sourceMappingURL=main.c4b75096.chunk.js.map