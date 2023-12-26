from src.server.routers import car, order, polomka, post, repair_shop, service, spareparts, staff, users


routers = (car.router, order.router, post.router,
           repair_shop.router, staff.router,
           polomka.router, users.router, service.router, spareparts.router)