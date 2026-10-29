import React from 'react';
import {AbsoluteFill,Composition,interpolate,registerRoot,useCurrentFrame,useVideoConfig} from 'remotion';
import data from './props.json';
type Props=typeof data;
const Film:React.FC<Props>=(p)=>{
 const frame=useCurrentFrame();const {fps,width,height}=useVideoConfig();const vertical=height>width;
 const seconds=frame/fps;const chapter=Math.min(4,Math.floor(seconds/6));const local=frame%(fps*6);
 const opacity=interpolate(local,[0,10,fps*6-10,fps*6-1],[0,1,1,0],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 const move=interpolate(local,[0,18],[30,0],{extrapolateRight:'clamp'});
 const slide=chapter===0?{title:p.product,detail:p.audience,demo:'这次，三个小变化。'}:chapter===4?{title:'下一版，由你来写',detail:p.callToAction,demo:'输入 → 工程 → MP4'}:p.updates[chapter-1];
 return <AbsoluteFill style={{background:'#edf3f0',color:'#173d3d',fontFamily:'Arial, "PingFang SC", sans-serif',padding:vertical?40:48}}>
  <div style={{display:'flex',justifyContent:'space-between',fontSize:vertical?18:20,fontWeight:700}}><span>OPCBoost · by Cogine</span><span>{String(chapter+1).padStart(2,'0')} / 05</span></div>
  <div style={{flex:1,display:'flex',flexDirection:'column',justifyContent:'center',opacity,transform:`translateY(${move}px)`}}>
   <div style={{fontSize:16,letterSpacing:3,color:'#247267',marginBottom:20}}>RELEASE NOTES / 更新速览</div>
   <h1 style={{fontSize:vertical?48:64,lineHeight:1.18,margin:'0 0 24px',maxWidth:width-90}}>{slide.title}</h1>
   <p style={{fontSize:vertical?26:28,lineHeight:1.55,maxWidth:700,margin:'0 0 34px'}}>{slide.detail}</p>
   <div style={{background:chapter===4?'#173d3d':'#fff',color:chapter===4?'#fff':'#247267',border:'2px solid #c1d8cc',borderRadius:20,padding:vertical?'28px 24px':'24px 30px',fontSize:vertical?28:30,fontWeight:700}}>{slide.demo}</div>
  </div>
  <div style={{height:5,background:'#ccddd3',borderRadius:8,marginBottom:18}}><div style={{height:5,width:`${frame/(fps*30-1)*100}%`,background:'#ed784c',borderRadius:8}}/></div>
 </AbsoluteFill>;
};
const Root=()=> <><Composition id="Landscape" component={Film} durationInFrames={720} fps={24} width={960} height={540} defaultProps={data}/><Composition id="Portrait" component={Film} durationInFrames={720} fps={24} width={540} height={960} defaultProps={data}/></>;
registerRoot(Root);
