"""Original scene recipe for Blender 4.5. Run inside Blender, not system Python."""
import argparse
import json
from pathlib import Path
import sys
import bpy
from mathutils import Vector

parser = argparse.ArgumentParser()
parser.add_argument('--output-dir', required=True)
args = parser.parse_args(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else [])
out = Path(args.output_dir).resolve()
out.mkdir(parents=True, exist_ok=True)
data = json.loads((Path(__file__).parent / 'scene.json').read_text(encoding='utf-8'))
if set(data['camera']) != {'front', 'side'}:
    raise ValueError('camera must define front and side views')
if any((out / name).is_symlink() for name in ('front.png', 'side.png', 'scene.blend')):
    raise ValueError('output files must not be symbolic links')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def material(name, color):
    rgb = tuple(int(color[i:i+2], 16) / 255 for i in (1, 3, 5))
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*rgb, 1)
    return mat
mats = {k: material(k, v) for k, v in data['palette'].items()}

def box(name, at, scale, mat, bevel=0.08):
    bpy.ops.mesh.primitive_cube_add(size=1, location=at)
    ob = bpy.context.object
    ob.name = name
    ob.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    ob.data.materials.append(mats[mat])
    mod = ob.modifiers.new('rounded edges', 'BEVEL')
    mod.width, mod.segments = bevel, 3
    ob.modifiers.new('weighted normals', 'WEIGHTED_NORMAL')
    return ob

def ball(name, at, scale):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, location=at)
    ob=bpy.context.object
    ob.name=name
    ob.scale=scale
    ob.data.materials.append(mats['lobster'])
    for p in ob.data.polygons: p.use_smooth = True
    return ob
box('desk', (0,0,1.25), (4,2.6,.22),'desk')
for x in (-1.65,1.65):
    for y in (-1,1): box('leg',(x,y,.57),(.15,.15,1.1),'desk')
box('monitor foot',(0,.65,1.44),(.8,.5,.08),'desk')
box('monitor stem',(0,.75,1.8),(.12,.12,.7),'desk')
box('monitor body',(0,.8,2.3),(1.7,.16,1.1),'desk')
box('screen',(0,.7,2.3),(1.5,.04,.9),'screen',.02)
box('lamp base',(-1.45,.7,1.45),(.5,.5,.1),'lamp')
box('lamp stand',(-1.45,.7,2.05),(.08,.08,1.2),'lamp')
box('lamp shade',(-1.35,.65,2.65),(.65,.55,.28),'lamp')
ball('lobster body',(.85,-.55,1.6),(.38,.57,.2))
for x in (.4,1.3):
    ball('claw',(x,-.95,1.65),(.24,.28,.13))
for y,s in [(-.05,.22),(.18,.16)]: ball('tail',(.85,y,1.53),(s,.2,.12))
scene=bpy.context.scene
scene.render.engine='CYCLES'
scene.cycles.samples=24
scene.render.resolution_x,scene.render.resolution_y=data['resolution']
scene.render.resolution_percentage=100
scene.world.color=(.22,.22,.22)
bpy.ops.object.light_add(type='AREA',location=(2,-3,7))
bpy.context.object.data.energy=850
bpy.context.object.data.shape='DISK'
bpy.context.object.data.size=5
bpy.ops.object.camera_add()
cam=bpy.context.object
scene.camera=cam
cam.data.type='ORTHO'
cam.data.ortho_scale=6.2
for label, coords in data['camera'].items():
    cam.location=coords
    cam.rotation_euler=(Vector((0,0,1.3))-cam.location).to_track_quat('-Z','Y').to_euler()
    scene.render.filepath=str(out/f'{label}.png')
    bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=str(out/'scene.blend'))
print('Wrote actual Blender renders and scene:',out)
