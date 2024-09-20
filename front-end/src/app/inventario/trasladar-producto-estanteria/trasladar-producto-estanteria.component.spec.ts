import { ComponentFixture, TestBed } from '@angular/core/testing';
import  TrasladarProductoEstanteriaComponent  from './trasladar-producto-estanteria.component';

describe('TrasladarProductoEstanteriaComponent', () => {
  let component: TrasladarProductoEstanteriaComponent;
  let fixture: ComponentFixture<TrasladarProductoEstanteriaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TrasladarProductoEstanteriaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TrasladarProductoEstanteriaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
