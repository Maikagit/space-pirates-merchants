// Basic 3D space game using Three.js

let scene, camera, renderer;
let ship;
const clock = new THREE.Clock();

const speed = {
    value: 0,
    min: 0,
    max: 50,
    acceleration: 20
};
const rotationSpeed = 1.5; // radians per second
const keys = {};

function init() {
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x000000);

    camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(5, 10, 7.5);
    scene.add(light);
    scene.add(new THREE.AmbientLight(0x404040));

    ship = createShip();
    scene.add(ship);

    // simple planet
    const planet = new THREE.Mesh(
        new THREE.SphereGeometry(5, 32, 32),
        new THREE.MeshStandardMaterial({ color: 0x0033aa })
    );
    planet.position.set(50, 0, -100);
    scene.add(planet);

    // portal (gate)
    const gate = new THREE.Mesh(
        new THREE.TorusGeometry(3, 0.5, 16, 100),
        new THREE.MeshStandardMaterial({ color: 0xff00ff })
    );
    gate.position.set(-40, 10, -60);
    scene.add(gate);

    window.addEventListener('resize', onWindowResize, false);
    document.addEventListener('keydown', e => keys[e.code] = true);
    document.addEventListener('keyup', e => keys[e.code] = false);

    animate();
}

function createShip() {
    const ship = new THREE.Group();
    const body = new THREE.Mesh(
        new THREE.ConeGeometry(0.5, 2, 8),
        new THREE.MeshStandardMaterial({ color: 0xdddddd })
    );
    body.rotation.x = Math.PI / 2;
    ship.add(body);

    const wing1 = new THREE.Mesh(
        new THREE.BoxGeometry(0.1, 1.2, 0.3),
        new THREE.MeshStandardMaterial({ color: 0xff0000 })
    );
    wing1.position.set(-0.6, 0, 0.2);
    ship.add(wing1);

    const wing2 = wing1.clone();
    wing2.position.set(0.6, 0, 0.2);
    ship.add(wing2);

    ship.position.z = 5;
    return ship;
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function handleInput(delta) {
    if (keys['KeyW']) {
        speed.value = Math.min(speed.max, speed.value + speed.acceleration * delta);
    }
    if (keys['KeyS']) {
        speed.value = Math.max(speed.min, speed.value - speed.acceleration * delta);
    }

    if (keys['ArrowLeft'] || keys['KeyA']) {
        ship.rotation.y += rotationSpeed * delta;
    }
    if (keys['ArrowRight'] || keys['KeyD']) {
        ship.rotation.y -= rotationSpeed * delta;
    }
    if (keys['ArrowUp']) {
        ship.rotation.x += rotationSpeed * delta;
    }
    if (keys['ArrowDown']) {
        ship.rotation.x -= rotationSpeed * delta;
    }
    if (keys['KeyQ']) {
        ship.rotation.z += rotationSpeed * delta;
    }
    if (keys['KeyE']) {
        ship.rotation.z -= rotationSpeed * delta;
    }
}

function updateShip(delta) {
    const forward = new THREE.Vector3(0, 0, -1).applyQuaternion(ship.quaternion);
    ship.position.addScaledVector(forward, speed.value * delta);
}

function updateCamera() {
    const offset = new THREE.Vector3(0, 2, 5).applyQuaternion(ship.quaternion);
    camera.position.copy(ship.position).add(offset);
    const lookAt = new THREE.Vector3(0, 0, -10).applyQuaternion(ship.quaternion).add(ship.position);
    camera.lookAt(lookAt);
}

function animate() {
    requestAnimationFrame(animate);
    const delta = clock.getDelta();
    handleInput(delta);
    updateShip(delta);
    updateCamera();
    renderer.render(scene, camera);
}

init();
