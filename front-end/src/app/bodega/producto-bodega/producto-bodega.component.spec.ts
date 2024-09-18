import { ComponentFixture, TestBed } from '@angular/core/testing';
import ProductoBodegaComponent  from './producto-bodega.component';

describe('ProductoBodegaComponent', () => {
  let component: ProductoBodegaComponent;
  let fixture: ComponentFixture<ProductoBodegaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProductoBodegaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProductoBodegaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
