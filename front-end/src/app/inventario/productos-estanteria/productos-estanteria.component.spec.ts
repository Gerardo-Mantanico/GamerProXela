import { ComponentFixture, TestBed } from '@angular/core/testing';
import  ProductosEstanteriaComponent  from './productos-estanteria.component';

describe('ProductosEstanteriaComponent', () => {
  let component: ProductosEstanteriaComponent;
  let fixture: ComponentFixture<ProductosEstanteriaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProductosEstanteriaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProductosEstanteriaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
