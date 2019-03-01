import sphere
import AGC

def main():
    s = sphere.Sphere()
    ag = AGC.AGC(32, 8, 4000, 0.02, s)
    ag.run()
    for i in ag._individuos:
        print(i._cromosoma)

if __name__ == '__main__':
    main()
