#!/usr/bin/python3

import subprocess

def run_docker_container(container_name):
    try:
        output = subprocess.check_output(
            ["sudo", "docker", "run", "-dit", "--name", container_name, "centos:7"],
            stderr=subprocess.STDOUT,
            text=True,
        )
        docker_ps = subprocess.check_output(
            ["sudo", "docker", "ps"],
            stderr=subprocess.STDOUT,
            text=True,
        )
        return output, docker_ps
    except subprocess.CalledProcessError as e:
        return f"Error: {e}", ""

def main():
    container_name = input("Enter a name for the Docker container: ")
    
    if not container_name:
        print("Error: Container name not provided.")
        return
    
    output, docker_ps = run_docker_container(container_name)
    
    print("Output:")
    print(output)
    print("Docker PS:")
    print(docker_ps)

if __name__ == "__main__":
    main()
