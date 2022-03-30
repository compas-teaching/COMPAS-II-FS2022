def show_trajectory(trajectory):
    import matplotlib.pyplot as plt
    # visualise
    positions = []
    velocities = []
    accelerations = []
    time_from_start = []

    for p in trajectory.points:
        positions.append(p.positions)
        velocities.append(p.velocities)
        accelerations.append(p.accelerations)
        time_from_start.append(p.time_from_start.seconds)

    plt.rcParams['figure.figsize'] = [17, 4]
    plt.subplot(131)
    plt.title('positions')
    plt.plot(positions)
    plt.subplot(132)
    plt.plot(velocities)
    plt.title('velocities')
    plt.subplot(133)
    plt.plot(accelerations)
    plt.title('accelerations')
    plt.show()
