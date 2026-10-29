// Run after npm ci. Uses a supplied browser path or Remotion's default browser.
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {dirname,join} from 'node:path';
const root=dirname(fileURLToPath(import.meta.url));
const extra=process.env.REMOTION_BROWSER_EXECUTABLE?['--browser-executable='+process.env.REMOTION_BROWSER_EXECUTABLE]:[];
for(const [composition,file] of [['Landscape','landscape.mp4'],['Portrait','portrait.mp4']]){
 const result=spawnSync(process.execPath,[join(root,'node_modules/@remotion/cli/remotion-cli.js'),'render','src.tsx',composition,file,'--concurrency=2','--crf=24',...extra],{cwd:root,stdio:'inherit'});
 if(result.error)throw result.error;
 if(result.status!==0)process.exit(result.status??1);
}
